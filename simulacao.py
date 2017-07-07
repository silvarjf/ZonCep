
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys
import execSimul
import sqlite3, pickle

### Interface para disparar simulações ###

Ui_MainWindow, QMainWindow = loadUiType('menuqt.ui')

tipossolo = ['1','2','3']
anos = list()
conn = sqlite3.connect('sarra.db')
cursor = conn.cursor()


# Carregar culturas e estados
cursor.execute('''
SELECT cultura.nome, configuracaoRegional.nomeConfiguracao, configuracaoRegional.id, grupo.nome, grupo.ID
FROM cultura, configuracaoRegional, grupo
WHERE cultura.id = configuracaoRegional.culturaID
AND configuracaoRegional.id = grupo.culturaRegiao
''')

tuplas = cursor.fetchall()

cursor.execute('''
SELECT estado.sigla
FROM estado
''')
estados = cursor.fetchall()
estadotmp = list()
for estado in estados:
    estadotmp.append(estado[0])
estados = estadotmp

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnSimular.clicked.connect(self.simular)
        self.btnAnos.clicked.connect(self.anoswindow)
        self.btnAddAno.clicked.connect(self.adicionaano)
        self.btnRmAno.clicked.connect(self.removeano)
        self.btnFechadock.clicked.connect(self.escondedock)
        self.cboxCultura.currentIndexChanged.connect(self.carregaConfReg)
        self.dwAnos.hide()
        self.cboxEstado.clear()
        self.cboxEstado.addItems(estados)
        self.cboxSolo.clear()
        self.cboxSolo.addItems(tipossolo)
        self.cboxConfReg.clear()
        self.cboxGrupo.clear()
        self.cboxConfReg.currentIndexChanged.connect(self.carregaGrupo)
        culturas = {tupla[0] for tupla in tuplas}
        self.cboxCultura.addItems(culturas)

    def simular(self):
        #print("simulando")
        #subprocess.Popen("python intersarra.py", shell=True)
        estado = str(self.cboxEstado.currentText())
        inisim = str(self.dteIniSim.date().toPyDate())
        dataplantio = str(self.dtePlantio.date().toPyDate())
        tiposolo = str(self.cboxSolo.currentText())
        tipocultura = str(self.cboxCultura.currentText())
        confregional = str(self.cboxConfReg.currentText())
        estoqueini = str(self.sbEstoqueInicial.value())
        chuvalimite = str(self.sbChuvaLimite.value())
        mulch = str(self.sbMulch.value())
        rusurf = str(self.sbRUSURF.value())
        resutil = str(self.sbReservaUtil.value())
        escsup = str(self.sbEscoamentoSup.value())
        for tupla in tuplas:
            if tupla[0] == self.cboxCultura.currentText() and tupla[1] == self.cboxConfReg.currentText() and tupla[3] == self.cboxGrupo.currentText():
                idgrupo = tupla[4]

        execSimul.simular(estado, inisim, dataplantio, tiposolo, idgrupo, estoqueini, chuvalimite, mulch, rusurf, resutil, escsup, anos)
        #QtCore.QCoreApplication.instance().quit()

    def carregaConfReg(self):
        self.cboxConfReg.clear()
        confreglist = []
        for tupla in tuplas:
            if tupla[0] == self.cboxCultura.currentText():
                confreglist.append(tupla[1])
        confreglist = set(confreglist)
        self.cboxConfReg.addItems(confreglist)

    def carregaGrupo(self):
        self.cboxGrupo.clear()
        grupolist = []
        for tupla in tuplas:
            if tupla[1] == self.cboxConfReg.currentText():
                grupolist.append(tupla[3])
        grupolist = set(grupolist)
        self.cboxGrupo.addItems(grupolist)

    def anoswindow(self):
        isVis = self.dwAnos.isVisible()
        if(isVis == True):
            self.dwAnos.hide()
        else:
            self.dwAnos.show()
            self.dwAnos.move(self.btnAnos.mapToGlobal(QtCore.QPoint(30,30)))

    def adicionaano(self):
        self.lvAnos.addItem(str(self.sbAnos.value()))
        anos.append(str(self.sbAnos.value()))

    def removeano(self):
            if(len(self.lvAnos.selectedIndexes()) > 0):
                item = self.lvAnos.currentItem()
                value = item.text()
                anos.remove(str(value))
                self.lvAnos.takeItem(self.lvAnos.currentRow())


    def escondedock(self):
        self.dwAnos.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
