#!/usr/bin/python3
# One Dimensional Cellular Automata GUI
#Author: Cristhian Eduardo Fuertes Daza
from gi.repository import Gtk, Gdk
import CellularAutomata
import sys

#The UI definitions specified in an XML format for the menu bar of the GUI
UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='AppMenu'>
      <menuitem action='Evolve' />
      <menuitem action='Clean and Restart' />
      <menuitem action='Quit' />
    </menu>
  </menubar>
</ui>
"""

#Initial Window use for the user to initialize the variables:
#Rule to be apply and the number of generations
class RulesDialog(Gtk.Window):
    #Constructor 
    def __init__(self):
        super(RulesDialog, self).__init__(title="Cellular Automata")
        self.set_size_request(150, 220)
        self.selected_rule = "";
        label1 = Gtk.Label("Select one of the above rules");
        label2 = Gtk.Label("Specify the number of generations");
        self.selected_rule = "Rule 30"
        rule_store = Gtk.ListStore(str)
        rule_store.append(['Rule 30'])
        rule_store.append(['Rule 54'])
        rule_store.append(['Rule 60'])
        rule_store.append(['Rule 62'])
        rule_store.append(['Rule 90'])
        rule_store.append(['Rule 94'])
        rule_store.append(['Rule 102'])
        rule_store.append(['Rule 110'])
        rule_store.append(['Rule 122'])
        rule_store.append(['Rule 126'])
        rule_store.append(['Rule 150'])
        rule_store.append(['Rule 158'])
        rule_store.append(['Rule 182'])
        rule_store.append(['Rule 188'])
        rule_store.append(['Rule 190'])
        rule_store.append(['Rule 220'])
        rule_store.append(['Rule 222'])
        rule_store.append(['Rule 250'])
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        rule_combo = Gtk.ComboBox.new_with_model(rule_store)
        rule_combo.connect("changed", self.__on_rule_combo_change)
        renderer_text = Gtk.CellRendererText()
        rule_combo.pack_start(renderer_text, False)
        rule_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(label1, False, False, False)
        vbox.pack_start(rule_combo, False, False, False)
        vbox.pack_start(label2, False, False, True)
        adjustment = Gtk.Adjustment(20, 20, 60, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_value(20)
        self.spinbutton.set_adjustment(adjustment)
        vbox.pack_start(self.spinbutton, False, False, False)
        button = Gtk.Button('OK')
        button.connect("clicked", self.__on_button_clicked)
        vbox.pack_start(button, False, False, False)
        self.add(vbox)
        self.show_all()
        self.connect('delete-event', Gtk.main_quit)
        Gtk.main()
    
    #Callback function for the OK button
    def __on_button_clicked(self, button):
        self.set_visible(False)
        gen = int(self.spinbutton.get_value())
        Window(self.selected_rule, gen, self)
        
        
        
    #Callback function for the combo box
    def __on_rule_combo_change(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            self.selected_rule = model[tree_iter][0]
            

#Main Window for the application. It displays the lattice of cells, allows
#the user to modify the state of the cells in generation zero and also allow to
#begin the simulation and exit/restart the application.
class Window(Gtk.Window):
    #Constructor
    # params:
    # rule_name -> string representing the selected rule
    # gen -> the number of generations for the simulation
    # dialog -> pointer to the initial dialog 
    def __init__(self, rule_name, gen, dialog):
        super(Window, self).__init__(title="One Dimensional Cellular Automata")
        # Attritue determinating the number of cells in each generation
        self.__num_cells = 100;
        self.__generations = gen
        self.__CA = CellularAutomata.CellularAutomata(self.__num_cells, rule_name)
        self.__scroll = Gtk.ScrolledWindow()
        self.fix = Gtk.Fixed()
        self.add(self.fix)
        self.__built_menu_bar()
        self.__built_lattice()
        self.dialog = dialog
        self.connect('delete-event', self.__gui_quit)
        self.show_all()
        Gtk.main()
        
    #Callback function for the close button in Window    
    def __gui_quit(self, par1, par2):
        sys.exit(0)
        
    #Creates the menu bar widget, menu widget and actions
    def __built_menu_bar(self):
        action_group = Gtk.ActionGroup("my_actions")
        self.__add_app_menu_actions(action_group)
        uimanager = self.__create_ui_manager()
        uimanager.insert_action_group(action_group)
        #Menu bar widget
        self.__menubar = uimanager.get_widget("/MenuBar")
        self.__menubar.set_size_request(840, 0)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(self.__menubar, True, True, 0)
        box.show()
        self.__menubar.show()
        self.__menubar.reparent(self.fix)
        
    #Adds menu action to menu bar
    #params:
    #action_group -> action group object to add actions
    def __add_app_menu_actions(self, action_group):
        action_appmenu = Gtk.Action("AppMenu", "Application", None, None)
        self.__action_evolve = Gtk.Action("Evolve", "Evolve", None, Gtk.STOCK_INDEX)
        self.__action_evolve.set_sensitive(False)
        action_clean_restart = Gtk.Action("Clean and Restart", "Clean and Restart",
                                           None, Gtk.STOCK_INDEX)
        action_quit = Gtk.Action("Quit", "Quit", None, Gtk.Label("_Cancel"))
        self.__action_evolve.connect('activate', self.__on_evolve_clicked)
        action_clean_restart.connect('activate', self.__on_clean_restart_clicked)
        action_quit.connect('activate', self.__on_quit_clicked)
        action_group.add_action(action_appmenu)
        action_group.add_action(self.__action_evolve)
        action_group.add_action(action_clean_restart)
        action_group.add_action(action_quit)
    
    #Callback function for menu item 'Clean and Restart'
    def __on_clean_restart_clicked(self, menuitem):
        self.dialog.destroy()
        self.destroy()
        RulesDialog()
    
    #Callback function for menu item 'Quit'
    def __on_quit_clicked(self, menuitem):
        sys.exit(0)
        
    #Callback function for menu item 'Evolve'
    def __on_evolve_clicked(self, menuitem):
        self.__evolve()
        self.__action_evolve.set_sensitive(False)
        
    #Creates UIManager object using XML description
    def __create_ui_manager(self):
        uimanager = Gtk.UIManager()     
        try:
            uimanager.add_ui_from_string(UI_INFO)
        except Exception as ex:
            print(('UI Manager Error: ', ex))
            sys.exit(1)
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager
    
    #Filter the cells in lattice to apply rules
    def __filter_lattice(self, i):
    	output = []
    	for j in range(1, self.__num_cells - 1):
    		if self.__matrix[i][j] == 1 or self.__matrix[i][j + 1] == 1 or self.__matrix[i][j - 1] == 1:
    			output.append(j)
    	return output

    #Initialize  the simulation using Cellular Automata object
    def __evolve(self):
    	for g in range(0, self.__generations - 1):
    		cell_list = self.__filter_lattice(g)
    		self.__CA.apply_rule(cell_list, self.__matrix,self.__lattice, g)

    #Creates the lattice of cells using Gtk Buttons and stablish event managing
    def __built_lattice(self):
        self.evolve_flag = 0;
        self.__matrix = []
       
        def callback(*args):
            col = args[len(args) - 1]
            if self.__matrix[0][col] == 0:
                self.__matrix[0][col] = 1
                self.__lattice.get_child_at(col, 0).set_opacity(0.0)
                self.evolve_flag += 1
            else:
                self.__matrix[0][col] = 0
                self.__lattice.get_child_at(col, 0).set_opacity(1.0)
                self.evolve_flag -= 1
            
            if self.evolve_flag > 0:
            	self.__action_evolve.set_sensitive(True)
            elif self.evolve_flag == 0:
            	self.__action_evolve.set_sensitive(False)

        
        
        self.__lattice = Gtk.Grid()
        self.__lattice.modify_bg(Gtk.StateFlags.NORMAL,
                                                Gdk.color_parse('green'))
        self.__lattice.set_row_spacing(0)
        self.__lattice.set_column_spacing(0)
        for i in range(0, self.__generations):
            row = [0] * self.__num_cells
            self.__matrix.append(row)
            for j in range(0, self.__num_cells):
                
                cell = Gtk.Button()
                cell.set_size_request(1, 1)
                if i == 0:
                    cell.connect('button-press-event', callback, j)
                else:
                    cell.set_sensitive(True)

                self.__lattice.attach(cell, j, i, 1, 1)
                
        self.__scroll.set_policy(Gtk.PolicyType.ALWAYS,
                               Gtk.PolicyType.ALWAYS)
        self.__scroll.add(self.__lattice)
        self.__lattice.reparent(self.fix)


#Call to RulesDialog to initialize GUI application
try:
    RulesDialog()
except Exception as ex:
    print("Execution error: ", ex)
    sys.exit(1)
