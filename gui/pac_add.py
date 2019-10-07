import tkinter as tk
import tkinter.ttk as ttk
import sys

sys.path.append('../database/')
from pac_db import PacientesDB

class PacienteAdd(ttk.Frame):
    """..."""
    def __init__(self, pacwin, addwin, *args, **kwargs):
        ttk.Frame.__init__(self, addwin)
        self.pacwin = pacwin
        self.addwin = addwin
        self.addwin.title("Adicionar Paciente")

        #self.window_geometry(300,200)
        self.create_frames()
        self.create_entries()
        self.create_buttons()

    # <<--------------- Class Methods -------------->>
    def window_geometry(self, width, height):
        """..."""
        self.scr_width = self.addwin.winfo_screenwidth()
        self.scr_height = self.addwin.winfo_screenheight()
        self.x = (self.scr_width / 2) # - (width / 2)
        self.y = (self.scr_height / 2) # - (height / 2)
        self.addwin.geometry('%dx%d+%d+%d' % (300, 200, self.x, self.y))

    def create_frames(self):
        # MainFrame
        self.mainframe = ttk.LabelFrame(self.addwin)
        self.mainframe.configure(text='Adicionar Paciente')
        self.mainframe.configure(labelanchor="n")
        self.mainframe.pack(pady=5)
        # Name Entry Frame
        self.name_fr = ttk.Frame(self.mainframe)
        self.name_fr.pack()
        # RG Entry Frame
        self.rg_fr = ttk.Frame(self.mainframe)
        self.rg_fr.pack()
        # SUS Entry Frame
        self.sus_fr = ttk.Frame(self.mainframe)
        self.sus_fr.pack()
        #Buttons Frames
        self.buttons_fr = ttk.Frame(self.mainframe)
        self.buttons_fr.pack(pady=8)


    def create_entries(self):
        """."""
        self.name_lbl = ttk.Label(self.name_fr, text="Nome:")
        self.name_lbl.configure(width=5)
        self.name_lbl.pack(side="left")
        self.name_entry = ttk.Entry(self.name_fr)
        self.name_entry.configure(width=40)
        self.name_val = tk.StringVar()
        self.name_entry.configure(textvariable=self.name_val)
        self.name_entry.pack(side="left")

        self.rg_lbl = ttk.Label(self.rg_fr, text="RG:")
        self.rg_lbl.configure(width=5)
        self.rg_lbl.pack(side="left")
        self.rg_entry = ttk.Entry(self.rg_fr)
        self.rg_entry.configure(width=15)
        self.rg_val = tk.StringVar()
        self.rg_entry.configure(textvariable=self.rg_val)
        self.rg_entry.pack(side="left")

        self.sus_lbl = ttk.Label(self.sus_fr, text="SUS:")
        self.sus_lbl.configure(width=5)
        self.sus_lbl.pack(side="left")
        self.sus_entry = ttk.Entry(self.sus_fr)
        self.sus_entry.configure(width=16)
        self.sus_val = tk.StringVar()
        self.sus_entry.configure(textvariable=self.sus_val)
        self.sus_entry.pack(side="left")

    # <<----- Event Handlers ------>>
    def save_data(self, event):
        """."""
        self._name_val = self.name_val.get()
        self._rg_val = self.rg_val.get()
        self._sus_val = self.sus_val.get()

        PacientesDB.add_paciente(self, self._name_val, self._rg_val, self._sus_val)

        self._name_val = self.name_val.set("")
        self._rg_val = self.rg_val.set("")
        self._sus_val = self.sus_val.set("")

    def quit_win(self, event):
        self.addwin.destroy()

    def create_buttons(self):
        """..."""
        self.save_button = ttk.Button(self.buttons_fr)
        self.save_button.configure(width=10, text="Salvar")
        self.save_button.bind("<Button-1>", self.save_data)
        self.save_button.pack(side="left")

        self.cancel_button = ttk.Button(self.buttons_fr)
        self.cancel_button.configure(width=10, text="Cancelar")
        self.cancel_button.bind("<Button-1>", self.quit_win)
        self.cancel_button.pack(side="left")
