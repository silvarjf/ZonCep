

# Variáveis calculadas diariamente no balanço hídrico
def VariaveisBalHidrico(parametros):

    varSaida = {}
    #
    varSaida['ETP'] = 0
    varSaida['Esc'] = 0
    varSaida['Apport'] = 0
    varSaida['Kc'] = 1
    varSaida['Evs'] = 0
    varSaida['Hum'] = parametros.ESTOQUEINICIAL
    varSaida['Dr'] = 0
    varSaida['Vrad'] = 0
    varSaida['StRurMax'] = 0
    varSaida['Hr'] = 0
    varSaida['Epc'] = 0
    varSaida['Etr'] = 0
    varSaida['Etm'] = 0
    varSaida['Eps'] = 0
    varSaida['StRur'] = 0
    varSaida['StRuSurf'] = 0
    varSaida['StRu'] = parametros.ESTOQUEINICIAL
    varSaida['TP'] = 0
    varSaida['EtrEtm'] = 0

    return varSaida



# Parametros de simulacao do balanco hidrico
class ParamSimul():
    def __init__(self):
        ### Valores default para as seguintes variaveis. O usuario pode alterar esses valores
        self.ESTOQUEINICIAL = 0
        self.chuvaLimite = 30
        self.mulch = 0.7
        self.RUSURF = 20
        self.RESERVAUTIL = 200
        self.tipoSolo = 1
        self.escoamentoSuperficial = 20
        self.anosDadosHistoricos = [2011]

        ### As datas de plantio e colheita devem ser definidas pelo usuario
        self.inicioSimul = (1, 1)
        self.fimSimul = (12, 31)
        self.inicioPlantio = (1, 6)
        self.diaColheita = (4, 15)