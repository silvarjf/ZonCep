# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuqt.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 1030)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblEstado = QtWidgets.QLabel(self.centralwidget)
        self.lblEstado.setObjectName("lblEstado")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblEstado)
        self.cboxEstado = QtWidgets.QComboBox(self.centralwidget)
        self.cboxEstado.setObjectName("cboxEstado")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cboxEstado)
        self.lblInicioSim = QtWidgets.QLabel(self.centralwidget)
        self.lblInicioSim.setObjectName("lblInicioSim")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInicioSim)
        self.dteIniSim = QtWidgets.QDateEdit(self.centralwidget)
        self.dteIniSim.setObjectName("dteIniSim")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dteIniSim)
        self.lblDataPlantio = QtWidgets.QLabel(self.centralwidget)
        self.lblDataPlantio.setObjectName("lblDataPlantio")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblDataPlantio)
        self.dtePlantio = QtWidgets.QDateEdit(self.centralwidget)
        self.dtePlantio.setObjectName("dtePlantio")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dtePlantio)
        self.lblAnosDados = QtWidgets.QLabel(self.centralwidget)
        self.lblAnosDados.setObjectName("lblAnosDados")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAnosDados)
        self.btnAnos = QtWidgets.QToolButton(self.centralwidget)
        self.btnAnos.setObjectName("btnAnos")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btnAnos)
        self.lblSolo = QtWidgets.QLabel(self.centralwidget)
        self.lblSolo.setObjectName("lblSolo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblSolo)
        self.cboxSolo = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSolo.setObjectName("cboxSolo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cboxSolo)
        self.lblCultura = QtWidgets.QLabel(self.centralwidget)
        self.lblCultura.setObjectName("lblCultura")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblCultura)
        self.cboxCultura = QtWidgets.QComboBox(self.centralwidget)
        self.cboxCultura.setObjectName("cboxCultura")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cboxCultura)
        self.lblConfigRegional = QtWidgets.QLabel(self.centralwidget)
        self.lblConfigRegional.setObjectName("lblConfigRegional")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblConfigRegional)
        self.cboxConfReg = QtWidgets.QComboBox(self.centralwidget)
        self.cboxConfReg.setObjectName("cboxConfReg")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cboxConfReg)
        self.cboxGrupo = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGrupo.setObjectName("cboxGrupo")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.cboxGrupo)
        self.lblGrupo = QtWidgets.QLabel(self.centralwidget)
        self.lblGrupo.setObjectName("lblGrupo")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lblGrupo)
        self.verticalLayout.addLayout(self.formLayout)
        self.gbParametros = QtWidgets.QGroupBox(self.centralwidget)
        self.gbParametros.setObjectName("gbParametros")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbParametros)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblEstoqueInicial = QtWidgets.QLabel(self.gbParametros)
        self.lblEstoqueInicial.setObjectName("lblEstoqueInicial")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblEstoqueInicial)
        self.sbEstoqueInicial = QtWidgets.QSpinBox(self.gbParametros)
        self.sbEstoqueInicial.setObjectName("sbEstoqueInicial")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sbEstoqueInicial)
        self.lblChuvaLimite = QtWidgets.QLabel(self.gbParametros)
        self.lblChuvaLimite.setObjectName("lblChuvaLimite")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblChuvaLimite)
        self.sbChuvaLimite = QtWidgets.QSpinBox(self.gbParametros)
        self.sbChuvaLimite.setObjectName("sbChuvaLimite")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sbChuvaLimite)
        self.lblMulch = QtWidgets.QLabel(self.gbParametros)
        self.lblMulch.setObjectName("lblMulch")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblMulch)
        self.lblRusurf = QtWidgets.QLabel(self.gbParametros)
        self.lblRusurf.setObjectName("lblRusurf")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblRusurf)
        self.sbRUSURF = QtWidgets.QSpinBox(self.gbParametros)
        self.sbRUSURF.setObjectName("sbRUSURF")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbRUSURF)
        self.lblReservaUtil = QtWidgets.QLabel(self.gbParametros)
        self.lblReservaUtil.setObjectName("lblReservaUtil")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblReservaUtil)
        self.sbReservaUtil = QtWidgets.QSpinBox(self.gbParametros)
        self.sbReservaUtil.setObjectName("sbReservaUtil")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sbReservaUtil)
        self.lblEscoamentoSup = QtWidgets.QLabel(self.gbParametros)
        self.lblEscoamentoSup.setObjectName("lblEscoamentoSup")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblEscoamentoSup)
        self.sbEscoamentoSup = QtWidgets.QSpinBox(self.gbParametros)
        self.sbEscoamentoSup.setObjectName("sbEscoamentoSup")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sbEscoamentoSup)
        self.sbMulch = QtWidgets.QDoubleSpinBox(self.gbParametros)
        self.sbMulch.setObjectName("sbMulch")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sbMulch)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.gbParametros)
        self.btnSimular = QtWidgets.QPushButton(self.centralwidget)
        self.btnSimular.setObjectName("btnSimular")
        self.verticalLayout.addWidget(self.btnSimular)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dwAnos = QtWidgets.QDockWidget(MainWindow)
        self.dwAnos.setFloating(True)
        self.dwAnos.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable)
        self.dwAnos.setObjectName("dwAnos")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lvAnos = QtWidgets.QListWidget(self.dockWidgetContents_3)
        self.lvAnos.setObjectName("lvAnos")
        self.verticalLayout_3.addWidget(self.lvAnos)
        self.sbAnos = QtWidgets.QSpinBox(self.dockWidgetContents_3)
        self.sbAnos.setMaximum(9999)
        self.sbAnos.setObjectName("sbAnos")
        self.verticalLayout_3.addWidget(self.sbAnos)
        self.btnAddAno = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.btnAddAno.setObjectName("btnAddAno")
        self.verticalLayout_3.addWidget(self.btnAddAno)
        self.btnRmAno = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.btnRmAno.setObjectName("btnRmAno")
        self.verticalLayout_3.addWidget(self.btnRmAno)
        self.btnFechadock = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.btnFechadock.setObjectName("btnFechadock")
        self.verticalLayout_3.addWidget(self.btnFechadock)
        self.dwAnos.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dwAnos)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.lblEstado.setText(_translate("MainWindow", "Estado:"))
        self.lblInicioSim.setText(_translate("MainWindow", "Início da Simulação:"))
        self.dteIniSim.setDisplayFormat(_translate("MainWindow", "dd/MM"))
        self.lblDataPlantio.setText(_translate("MainWindow", "Data do Plantio:"))
        self.dtePlantio.setDisplayFormat(_translate("MainWindow", "dd/MM"))
        self.lblAnosDados.setText(_translate("MainWindow", "Anos dos Dados Históricos:"))
        self.btnAnos.setText(_translate("MainWindow", "..."))
        self.lblSolo.setText(_translate("MainWindow", "Tipo de Solo:"))
        self.lblCultura.setText(_translate("MainWindow", "Cultura:"))
        self.lblConfigRegional.setText(_translate("MainWindow", "Configuração Regional:"))
        self.lblGrupo.setText(_translate("MainWindow", "Grupo:"))
        self.gbParametros.setTitle(_translate("MainWindow", "Parâmetros"))
        self.lblEstoqueInicial.setText(_translate("MainWindow", "Estoque Inicial:"))
        self.lblChuvaLimite.setText(_translate("MainWindow", "Chuva Limite:"))
        self.lblMulch.setText(_translate("MainWindow", "Mulch:"))
        self.lblRusurf.setText(_translate("MainWindow", "RUSURF:"))
        self.lblReservaUtil.setText(_translate("MainWindow", "Reserva Útil:"))
        self.lblEscoamentoSup.setText(_translate("MainWindow", "Escoamento Superficial:"))
        self.btnSimular.setText(_translate("MainWindow", "Simular"))
        self.btnAddAno.setText(_translate("MainWindow", "Adicionar"))
        self.btnRmAno.setText(_translate("MainWindow", "Remover"))
        self.btnFechadock.setText(_translate("MainWindow", "Fechar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
