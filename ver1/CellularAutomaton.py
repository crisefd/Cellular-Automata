#Cellular Automaton
from gi.repository import Gtk, Gdk
#Pango
#from gi.repository import GdkPixbuf
import random
hight = 30
width = 100


class Window(Gtk.Window):

    def __init__(self):
        super(Window, self).__init__()
        #super(Window, self).__init__(title="Cellular Automaton")
        self.set_size_request(940, 940)
        self.set_resizable(False)
        self.fix = Gtk.Fixed()
        self.add(self.fix)
        self.__builtLattice(width, hight)
        self.connect('delete-event', Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def __builtLattice(self, width, height):
        self.matrix = []
        #colors = ['green', 'blue']
        self.lattice = Gtk.Grid()
        self.lattice.set_size_request(940, 940)
        self.lattice.set_row_spacing(4)
        self.lattice.set_column_spacing(1)
        for i in range(0, height):
            row = [0] * width
            for j in range(0, width):
                self.matrix.append(row)
                label = Gtk.Label()
                label.set_size_request(10, 10)
                #p = random.randint(0, 1)
                label.modify_bg(Gtk.StateType.NORMAL,
                                                Gdk.color_parse('green'))
                self.lattice.attach(label, j, i, 1, 1)
        self.fix.put(self.lattice, 0, 0)


Window()