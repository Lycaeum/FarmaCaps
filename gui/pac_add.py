import tkinter as tk
import tkinter.ttk as ttk

class PacienteAdd(ttk.Frame):
    """..."""
    def __init__(self, pacwin, addwin, *args, **kwargs):
        ttk.Frame.__init__(self, addwin)
        self.pacwin = pacwin
        self.addwin = addwin
        self.addwin.title("Adicionar Paciente")

        self.create_frames()
        self.create_entries()

    def create_frames(self):
        # MainFrame
        self.mainframe = ttk.LabelFrame(self.addwin)
        self.mainframe.configure(text='Adicionar Paciente')
        self.mainframe.configure(labelanchor="n")
        self.mainframe.pack(pady=5)

        self.name_fr = ttk.Frame(self.mainframe)
        self.name_fr.pack()

        self.rg_fr = ttk.Frame(self.mainframe)
        self.rg_fr.pack()

        self.sus_fr = ttk.Frame(self.mainframe)
        self.sus_fr.pack()

    def create_entries(self):
        self.name_lbl = ttk.Label(self.name_fr, text="Nome:")
        self.name_lbl.configure(width=5)
        self.name_lbl.pack(side="left")
        self.name_entry = ttk.Entry(self.name_fr)
        self.name_entry.configure(width=40)
        self.name_entry.pack(side="left")

        self.rg_lbl = ttk.Label(self.rg_fr, text="RG:")
        self.rg_lbl.configure(width=5)
        self.rg_lbl.pack(side="left")
        self.rg_entry = ttk.Entry(self.rg_fr)
        self.rg_entry.pack(side="left")

        self.sus_lbl = ttk.Label(self.sus_fr, text="SUS:")
        self.sus_lbl.configure(width=5)
        self.sus_lbl.pack(side="left")
        self.sus_entry = ttk.Entry(self.sus_fr)
        self.sus_entry.pack(side="left")
