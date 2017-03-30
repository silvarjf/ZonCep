import sqlite3, pickle

class Cultura():
    def __init__(self):
        pass

    def carregarDoBD(self, ID):
        conn = sqlite3.connect('sarra.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM grupo, cultivares
        WHERE grupo.ID = %d AND grupo.cultura = cultivares.ID''' %
                       (ID))

        for linha in cursor.fetchall():
            self.culturaNome = linha[8]
            self.grupoNome = linha[1]
            self.duracaoCiclo = linha[3]
            self.tipoVrad = linha[4]
            self.tipoKc = linha[6]

            if self.tipoKc == 1:
                self.kc = pickle.loads(linha[7])



# cultura = Cultura()
# cultura.carregarDoBD(1)
# print('1')