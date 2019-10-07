""" FarmaCAPS.
    Gerenciamento de Database de pacientes
"""
import sqlite3

class PacientesDB:
    def __init__(self, pac_name, pac_rg, pac_sus):
        # Variaveis
        self._name = pac_name
        self._rg = pac_rg
        self._sus = pac_sus
        # Conexao com database 'pacientes.db' _e criacao de cursor
        self.pacdb = sqlite3.connect('./dbfiles/pacientes.db', mode=775)
        self.pacdb_cursor = self.pacdb.cursor()
        # -------------------- Comandos SQL --------------------
        # Deletar cadastro de paciente na 'pacientes.db'
        self.pacdb_delete = """ DELETE FROM pacientes
                                WHERE id=?
                            """
        # ----- Consulta tabela -----
        self.pacdb_query = """ SELECT * FROM pacientes """

    # <<--------------- Metodos da classe PacientesDB --------------->>



    # ----- Metodos de Gerenciamento -----
    def create_db(self):
        """ Criar nova Database """
        self.pacdb = sqlite3.connect('pacientes.db')
        self.pacdb_cursor = self.pacdb.cursor()
        self.pacdb_create = """ CREATE TABLE IF NOT EXISTS pacientes(
                                id      AUTO INCREMENT KEY
                                nome    TEXT(40) NOT NULL,
                                rg      TEXT(15) NOT NULL,
                                sus     TEXT(16) NOT NULL)
                            """
        self.pacdb_cursor.execute(self.pacdb_create)

    def add_paciente(self, _name, _rg, _sus):
        """ Inserir Cadastro depaciente """
        self._name = _name
        self._rg = _rg
        self._sus = _sus

        self.pacdb = sqlite3.connect('pacientes.db')
        self.pacdb_cursor = self.pacdb.cursor()

        self.pacdb_insert = """ INSERT INTO pacientes(nome,rg,sus)
                                VALUES(?,?,?)
                            """, (self._name, self._rg, self._sus)
        self.pacdb_cursor.execute(self.pacdb_insert)
        self.pacdb.commit()
        self.pacdb.close()

    def update_paciente(self):
        """ Altera o cadastro do paciente """
        self.pacdb_update = """ UPDATE pacientes """
        self.pacdb_cursor.execute(self.pacdb_update)
        self.pacdb.commit()
        self.pacdb.close()

    # ----- Metodos de Consulta -----
