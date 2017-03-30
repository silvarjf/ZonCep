from datetime import date

# Variáveis calculadas diariamente no balanço hídrico
class VariaveisBalHidrico():
    def __init__(self, parametros):

        #
        self.ETP = 0
        self.Esc = 0
        self.Apport = 0
        self.Kc = 1
        self.Evs = 0
        self.Hum = parametros.ESTOQUEINICIAL
        self.Dr = 0
        self.Vrad = 0
        self.StRurMax = 0
        self.Hr = 0
        self.Epc = 0
        self.Etr = 0
        self.Etm = 0
        self.Eps = 0
        self.StRur = 0
        self.StRuSurf = 0
        self.StRu = parametros.ESTOQUEINICIAL
        self.TP = 0
        self.EtrEtm = 0



# Parametros de simulacao do balanco hidrico
class ParamSimul():
    def __init__(self):
        ### Valores default para as seguintes variaveis. O usuario pode alterar esses valores
        self.ESTOQUEINICIAL = 0
        self.chuvaLimite = 30
        self.mulch = 0.7
        self.RUSURF = 20
        self.RESERVAUTIL = 200
        self.PROFMAXIMA = 350
        self.escoamentoSuperficial = 20
        self.anosDadosHistoricos = [2011]

        ### As datas de plantio e colheita devem ser definidas pelo usuario
        self.inicioSimul = date(2014, 1, 1)
        self.fimSimul = date(2014, 12, 31)
        self.inicioPlantio = date(2014, 1, 6)
        self.diaColheita = date(2014, 4, 15)