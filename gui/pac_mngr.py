import tkinter as tk
import tkinter.ttk as ttk

class PacienteManager(ttk.Frame):
    def __init__(self,pacwin, *args, **kwargs):
        ttk.Frame.__init__(self, pacwin)
        self.pacwin = pacwin
        self.pacwin.title('Database dos Pacientes')

        # Frames
        self.mainframe = ttk.LabelFrame(pacwin, text='Database dos Pacientes')
        self.mainframe.pack()
        self.field_data_fr = ttk.LabelFrame(self.mainframe, text='Dados')
        self.field_data_fr.pack()
        self.vis_fr = ttk.LabelFrame(self.mainframe, text='Visualizar')
        self.vis_fr.pack()

        self.lbl_name = ttk.Label(self.field_data_fr, text='Nome:')
        self.lbl_name.pack(side='left')
        self.entry_name = ttk.Entry(self.field_data_fr, width=40)
        self.entry_name.pack(side='left')

        self.lbl_rg = ttk.Label(self.field_data_fr, text='RG:')
        self.lbl_rg.pack(side='left')
        self.entry_rg = ttk.Entry(self.field_data_fr, width=15)
        self.entry_rg.pack(side='left')

        self.lbl_sus = ttk.Label(self.field_data_fr, text='SUS :')
        self.lbl_sus.pack(side='left')
        self.entry_sus = ttk.Entry(self.field_data_fr, width=16)
        self.entry_sus.pack(side='left')

        self.pac_tvw = ttk.Treeview(self.mainframe)
        self.pac_tvw.pack()


if __name__ == "__main__":
    def main():
        """ Main Function """
        app = tk.Tk()
        PacienteManager(app)
        app.mainloop()
main()
