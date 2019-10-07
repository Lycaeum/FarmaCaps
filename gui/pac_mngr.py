import tkinter as tk
import tkinter.ttk as ttk
import sys
sys.path.append('../database/')
from pac_db import PacientesDB
from pac_add import PacienteAdd

class PacienteManager(ttk.Frame):
    """."""
    def __init__(self, pacwin, *args, **kwargs):
        ttk.Frame.__init__(self, pacwin)
        self.pacwin = pacwin
        self.pacwin.title('Database dos Pacientes')

        self.create_frames()
        self.create_entries()
        self.create_text_dataout()
        self.create_buttons()

    def create_frames(self):
        """ Creates and manages all PacienteManager class frames """
        # MainFrame
        self.mainframe = ttk.LabelFrame(self.pacwin)
        self.mainframe.configure(text='Database dos Pacientes')
        self.mainframe.configure(labelanchor="n")
        self.mainframe.pack(pady=5)
        # Field Data Frame
        self.field_data_fr = ttk.LabelFrame(self.mainframe)
        self.field_data_fr.configure(text='Busca por Campo')
        self.field_data_fr.pack(pady=10)
        # Data Visualization Frame
        self.vis_fr = ttk.LabelFrame(self.mainframe, text='Visualizar')
        self.vis_fr.configure(labelanchor="n")
        self.vis_fr.pack(pady=6)
        # Buttons Frame
        self.but_fr = ttk.LabelFrame(self.mainframe)
        self.but_fr.configure(text="Operações")
        self.but_fr.configure(labelanchor="n")
        self.but_fr.pack()

        self.but_fr = ttk.Frame(self.mainframe)
        self.but_fr.pack(pady=8)
        self.buttons_left_int_fr = ttk.Frame(self.but_fr)
        self.buttons_left_int_fr.pack(side='left')
        self.buttons_right_int_fr = ttk.Frame(self.but_fr)
        self.buttons_right_int_fr.pack(side='left')

    def create_entries(self):
        """ Creates Entry Fields """
        self.lbl_name = ttk.Label(self.field_data_fr)
        self.lbl_name.configure(text='Nome :')
        self.lbl_name.pack(side='left')
        self.entry_name = ttk.Entry(self.field_data_fr, width=40)
        self.entry_name.pack(pady=3, side='left')

        self.lbl_rg = ttk.Label(self.field_data_fr)
        self.lbl_rg.configure(text='RG:')
        self.lbl_rg.pack(side='left')
        self.entry_rg = ttk.Entry(self.field_data_fr, width=15)
        self.entry_rg.pack(pady=3, side='left')

        self.lbl_sus = ttk.Label(self.field_data_fr)
        self.lbl_sus.configure(text='SUS :')
        self.lbl_sus.pack(side='left')
        self.entry_sus = ttk.Entry(self.field_data_fr, width=16)
        self.entry_sus.pack(pady=3, side='left')

    def create_text_dataout(self):
        """."""
        self.output_data_textbox = tk.Text(self.vis_fr)
        self.output_data_textbox.pack(pady=3, fill = "both", expand=True)

    def create_buttons(self):
        """."""
        self.sair_button = ttk.Button(self.buttons_right_int_fr)
        self.sair_button.configure(text="Sair", width=10)
        self.sair_button.bind("<Button-1>", self.quit)
        self.sair_button.pack(padx=2, side="left")

        self.alter_button = ttk.Button(self.buttons_right_int_fr)
        self.alter_button.configure(text="Alterar", width=10)
        self.alter_button.pack(padx=2, side="left")

        self.delete_button = ttk.Button(self.buttons_right_int_fr)
        self.delete_button.configure(text="Deletar", width=10)
        self.delete_button.pack(padx=2, side="left")

        self.add_button = ttk.Button(self.buttons_right_int_fr)
        self.add_button.configure(text="Adicionar", width=10)
        self.add_button.bind("<Button-1>", self.paciente_add)
        self.add_button.pack(padx=2, side="left")

        self.createdb_button = ttk.Button(self.buttons_left_int_fr)
        self.createdb_button.configure(text="Criar DB", width=10)
        self.createdb_button.bind("<Button-1>", self.create_db)
        self.createdb_button.pack(padx=2, side="left")

    def create_db(self, event):
        """..."""


    def paciente_add(self, event):
        """..."""
        self.pac_add_window = tk.Toplevel(self.pacwin)
        self.pac_add_class = PacienteAdd(self.pacwin, self.pac_add_window)

    def quit(self, event):
        """...."""
        self.pacwin.destroy()

if __name__ == "__main__":
    def main():
        """ Main Function """
        app = tk.Tk()
        PacienteManager(app).pack(fill="both", expand=True)
        app.mainloop()
main()
