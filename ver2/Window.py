#Cellular Automaton
from gi.repository import Gtk, Gdk
import CellularAutomata
#Pango
#from gi.repository import GdkPixbuf
#import random
hight = 30
width = 100


class Window(Gtk.Window):

    def __init__(self):
        #super(Window, self).__init__()
        super(Window, self).__init__(title="Cellular Automaton")
        self.__CA = CellularAutomata.CellularAutomata(width, 0)
        self.set_size_request(940, 940)
        self.set_resizable(False)
        self.fix = Gtk.Fixed()
        self.add(self.fix)
        self.__builtLattice(width, hight)
        #print('KKKK ', self.__lattice.get_child_at(99, 1))
        self.connect('delete-event', Gtk.main_quit)
        self.__evolution()
        self.show_all()
        
        Gtk.main()
        

    def __evolution(self):
        for t in range(0, hight - 1):
            self.__CA.applyRule(self.__matrix, self.__lattice, t)

    def __builtLattice(self, width, height):
        self.__matrix = []

        def callback(*args):
            col = args[len(args) - 1]
            if self.__matrix[0][col] == 0:
                #print('h')
                self.__matrix[0][col] = 1
                self.__lattice.get_child_at(col, 0).set_opacity(0.0)
            else:
                #print('k')
                self.__matrix[0][col] = 0
                self.__lattice.get_child_at(col, 0).set_opacity(1.0)
            #self.show_all()

        self.__lattice = Gtk.Grid()
        self.__lattice.modify_bg(Gtk.StateFlags.NORMAL,
                                                Gdk.color_parse('green'))
        self.__lattice.set_size_request(940, 940)
        self.__lattice.set_row_spacing(0)
        self.__lattice.set_column_spacing(0)
        #self.__lattice.connect('button-press-event', callback1)
        for i in range(0, height):
            row = [0] * width
            for j in range(0, width):
                self.__matrix.append(row)
                cell = Gtk.Button()
                cell.set_size_request(10, 10)
                #cell.override_background_color(Gtk.StateFlags.ACTIVE,
                #Gdk.RGBA(0, 0, 0, 0))
                #cell.modify_bg(Gtk.StateFlags.NORMAL,
                                                #Gdk.color_parse('green'))
                #cell.modify_fg(Gtk.StateFlags.NORMAL,
                                                #Gdk.color_parse('green'))
                if i == 0:
                    cell.connect('button-press-event', callback, j)
                    if j == 49:
                        cell.set_opacity(0.0)
                else:
                    cell.set_sensitive(True)

                self.__lattice.attach(cell, j, i, 1, 1)
        self.fix.put(self.__lattice, 0, 0)


Window()
