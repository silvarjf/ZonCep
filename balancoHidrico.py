from datetime import date, timedelta
from estrutura import VariaveisBalHidrico
from pyeto import deg2rad, daylight_hours, sunset_hour_angle, sol_dec
import calculosDecendiais


# Calculo dos ISNAS
class balancoHidrico():
    def __init__(self, estacao, cultura):

        self.estacao = estacao
        self.cultura = cultura


    # Calcular EtPs decendiais
    def etp_Thornthwaite(self):
        latitudeRad = deg2rad(self.estacao.latitude)

        ### Calcula medias mensais e decendiais de temperatura para um ano ###
        diaAtual = date(self.parametros.inicioSimul.year,
                           1, 1)
        ano = diaAtual.year

        temperaturaAcum = 0
        temperaturaAcumMes = 0
        diasNoDecendio = 0
        diasNoMes = 0

        temperaturaMensal = []
        temperaturaDecendio = {}

        while diaAtual.year == ano:
            if self.dadosTemperatura[diaAtual] is not None:
                temperaturaAcum += self.dadosTemperatura[diaAtual]
                temperaturaAcumMes += self.dadosTemperatura[diaAtual]
                diasNoDecendio += 1
                diasNoMes += 1

            amanha = diaAtual + timedelta(days=1)


            if amanha.month != diaAtual.month:
                if diasNoMes > 0:
                    # Corrigir temperaturas negativas
                    temperaturaMensal.append(temperaturaAcumMes/diasNoMes * (temperaturaAcumMes >= 0))
                else:
                    temperaturaMensal.append(25)

                temperaturaAcumMes = 0
                diasNoMes = 0

            if amanha.day == 1 or amanha.day == 11 or amanha.day == 21:
                decendioAtual = calculosDecendiais.converterToDataDecendio(diaAtual)
                if diasNoDecendio > 0:
                    temperaturaDecendio[decendioAtual] = (temperaturaAcum/diasNoDecendio) * (temperaturaAcum >= 0)
                else:
                    temperaturaDecendio[decendioAtual] = 25

                temperaturaAcum = 0
                diasNoDecendio = 0

            diaAtual = amanha

        ###########


        # Calcula o heat index a partir das temperaturas
        self.temperaturaMensal = temperaturaMensal
        I = 0.0
        for Tai in temperaturaMensal:
            if Tai / 5.0 > 0.0:
                I += (Tai / 5.0) ** 1.514

        a = (6.75e-07 * I ** 3) - (7.71e-05 * I ** 2) + (1.792e-02 * I) + 0.49239

        diaAtual = date(self.parametros.inicioSimul.year, 1, 1)
        ano = diaAtual.year

        ETPs = {}
        horasDeSolAcum = 0
        diasNoDecendio = 0

        # Calcula o valor dos ETPs decendiais
        while diaAtual.year == ano:
            sd = sol_dec(int(diaAtual.strftime('%j')))
            sha = sunset_hour_angle(latitudeRad, sd)
            horasDeSolAcum += daylight_hours(sha)


            diasNoDecendio += 1

            amanha = diaAtual + timedelta(days=1)

            if amanha.day == 1 or amanha.day == 11 or amanha.day == 21:
                horasDeSolMedia = horasDeSolAcum/diasNoDecendio

                decendioAtual = calculosDecendiais.converterToDataDecendio(diaAtual)
                ETPs[decendioAtual] = 1.6 * (horasDeSolMedia / 12.0) * (diasNoDecendio / 30.0) * ((10.0 * temperaturaDecendio[decendioAtual] / I) ** a) * 10.0
                horasDeSolAcum = 0
                diasNoDecendio = 0

            diaAtual = amanha

        return ETPs


    # Calcula o valor do ETP diario interpolando valores decendiais
    def calcularETP(self, dia):
        decendio = calculosDecendiais.converterToDataDecendio(dia)
        decendioFuturo = calculosDecendiais.proximoDecendio(decendio)
        etpAtual = self.ETPsDecendiais[decendio]
        etpFuturo = self.ETPsDecendiais[decendioFuturo]

        return (etpAtual + (etpFuturo - etpAtual) * ((dia - calculosDecendiais.inicioDecendio(dia)).days) / calculosDecendiais.diasNoDecendio(dia)) / 10


    # Importa os valores de precipitacao e temperatura da base de dados
    def lerDadosPrecTemp(self):
        dataInicial = date(self.parametros.inicioSimul.year,
                           1, 1)
        dataFinal = date(self.parametros.fimSimul.year, 12, 31)

        return self.estacao.lerDadosPrecTemp(dataInicial, dataFinal)


    def calcularEsc(self, diaAtual):
        enplus = self.dadosPrecipitacao[diaAtual] + self.dadosIrrigacao[diaAtual]
        esc = 0

        if enplus > self.parametros.chuvaLimite:
            esc = (enplus - self.parametros.chuvaLimite) * self.parametros.escoamentoSuperficial/100

        return esc


    def calcularApport(self, diaAtual, Esc):
        return self.dadosPrecipitacao[diaAtual] + self.dadosIrrigacao[diaAtual] - Esc



    def calcularEps(self, diaAtual, etp):
        return self.parametros.mulch * etp

    def rempliRu(self, Apport, StRu, Hum):
        StRuMax = self.parametros.RESERVAUTIL*self.parametros.PROFMAXIMA/1000
        StRu = StRu + Apport
        Dr = 0

        if StRu > StRuMax:
            Dr = StRu - StRuMax
            StRu = StRuMax

        Hum = max(Hum, StRu)
        return (StRu, Hum, Dr)

    def calcularKc(self, diaAtual):
        decendioAtual = (((diaAtual - self.parametros.inicioPlantio).days) // 10) + 1
        nDias = (diaAtual - self.parametros.inicioPlantio - timedelta((decendioAtual - 1) * 10)).days

        if decendioAtual - 1 < len(self.cultura.kc):
            kcAtual = self.cultura.kc[decendioAtual - 1]
        else:
            kcAtual = 1

        if decendioAtual < len(self.cultura.kc):
            kcProx = self.cultura.kc[decendioAtual]
        else:
            kcProx = 1

        return kcAtual + (kcProx - kcAtual)*nDias/calculosDecendiais.diasNoDecendio(diaAtual)

    def calcularVrad(self, Hum, StRurMax):
        vRad = 100*(Hum - StRurMax)/self.parametros.RESERVAUTIL
        deltaRur = min(Hum - StRurMax, vRad/1000*self.parametros.RESERVAUTIL)

        return vRad, deltaRur

    def calcularHr(self, StRur, StRurMax):
        Hr = 0

        if StRurMax > 0:
            Hr = StRur/StRurMax

        return Hr

    def calcularEtrEtm(self, Epc, ETP, Hr, Evs, StRur, Etm):
        Etr = Epc * (( -0.05 + 0.732/ETP) + (4.97 - 0.66*ETP) * Hr + (-8.57 + 1.56*ETP)*Hr*Hr + (4.35 - 0.88*ETP)*Hr*Hr*Hr)
        TP = Etr

        if Etr > Evs:
            Etm = Epc
            Etr = min(Etr, Etm)
            Etr = max(Etr, 0)
            Etr = min(StRur, Etr)
        else:
            Etr = Evs

        return Etr, Etm, TP


    ### Realiza os calculos do balanco hidrico com os dados especificados ###
    def simularBalancoHidrico(self, parametros):


        def preSemeio(diaAtual, varDiaAnterior):
            varDiaAtual = VariaveisBalHidrico(self.parametros)

            varDiaAtual.ETP = self.calcularETP(diaAtual)
            varDiaAtual.Hr = varDiaAnterior.Hr
            varDiaAtual.Kc = varDiaAnterior.Kc

            varDiaAtual.Esc = self.calcularEsc(diaAtual)
            varDiaAtual.Apport = self.calcularApport(diaAtual, varDiaAtual.Esc)

            varDiaAtual.Etm = self.calcularEps(diaAtual, varDiaAtual.ETP)
            varDiaAtual.Eps = 0
            varDiaAtual.Epc = 0

            varDiaAtual.StRuSurf = min(varDiaAnterior.StRuSurf + varDiaAtual.Apport, self.parametros.RUSURF)
            varDiaAtual.Evs = min(varDiaAtual.Etm * varDiaAtual.StRuSurf/self.parametros.RUSURF, varDiaAtual.StRuSurf)
            varDiaAtual.Etr = varDiaAtual.Evs

            (varDiaAtual.StRu, varDiaAtual.Hum, varDiaAtual.Dr) = self.rempliRu(varDiaAtual.Apport, varDiaAnterior.StRu, varDiaAnterior.Hum)

            varDiaAtual.StRu = max(varDiaAtual.StRu - varDiaAtual.Etr, 0)
            varDiaAtual.StRuSurf = max(varDiaAtual.StRuSurf - varDiaAtual.Etr, 0)

            varDiaAtual.Vrad = varDiaAnterior.Vrad
            varDiaAtual.StRur = varDiaAnterior.StRur
            varDiaAtual.StRurMax = varDiaAnterior.StRurMax
            varDiaAtual.TP = varDiaAnterior.TP
            varDiaAtual.EtrEtm = 100*varDiaAtual.Etr/varDiaAtual.Etm

            return varDiaAtual

        def fasesFenologicas(diaAtual, varDiaAnterior):
            varDiaAtual = VariaveisBalHidrico(self.parametros)

            varDiaAtual.ETP = self.calcularETP(diaAtual)

            varDiaAtual.Esc = self.calcularEsc(diaAtual)
            varDiaAtual.Apport = self.calcularApport(diaAtual, varDiaAtual.Esc)

            varDiaAtual.Kc = self.calcularKc(diaAtual)
            varDiaAtual.Eps = self.calcularEps(diaAtual, varDiaAtual.ETP)
            varDiaAtual.Etm = varDiaAtual.Eps

            varDiaAtual.StRuSurf = min(varDiaAnterior.StRuSurf + varDiaAtual.Apport, self.parametros.RUSURF)
            varDiaAtual.Evs = min(varDiaAtual.Eps * varDiaAtual.StRuSurf / self.parametros.RUSURF, varDiaAtual.StRuSurf)
            varDiaAtual.Etr = varDiaAtual.Evs

            (varDiaAtual.StRu, varDiaAtual.Hum, varDiaAtual.Dr) = self.rempliRu(varDiaAtual.Apport, varDiaAnterior.StRu,
                                                                                varDiaAnterior.Hum)

            if diaAtual == self.parametros.inicioPlantio:
                varDiaAtual.Vrad = varDiaAnterior.Vrad
                varDiaAtual.StRurMax = varDiaAnterior.StRurMax
                varDiaAtual.Hr = varDiaAnterior.Hr
                varDiaAtual.Epc = 0
                varDiaAtual.TP = varDiaAnterior.TP
                varDiaAtual.StRur = varDiaAnterior.StRur
            else:
                (varDiaAtual.Vrad, deltaRur) = self.calcularVrad(varDiaAtual.Hum, varDiaAnterior.StRurMax)
                varDiaAtual.StRurMax = varDiaAnterior.StRurMax + deltaRur
                varDiaAtual.StRur = min(varDiaAnterior.StRur + varDiaAtual.Apport + deltaRur, varDiaAtual.StRurMax, varDiaAtual.StRu)
                varDiaAtual.Hr = self.calcularHr(varDiaAtual.StRur, varDiaAtual.StRurMax)

                varDiaAtual.Epc = varDiaAtual.Kc*varDiaAtual.ETP

                (varDiaAtual.Etr, varDiaAtual.Etm, varDiaAtual.TP) = self.calcularEtrEtm(varDiaAtual.Epc, varDiaAtual.ETP, varDiaAtual.Hr, varDiaAtual.Evs, varDiaAtual.StRur, varDiaAtual.Etm)

                varDiaAtual.Eps = varDiaAtual.StRurMax - varDiaAtual.StRur
                varDiaAtual.StRur = max(varDiaAtual.StRur - varDiaAtual.Etr, 0)

            varDiaAtual.StRuSurf = max(varDiaAtual.StRuSurf - varDiaAtual.Etr, 0)
            varDiaAtual.StRu = max(varDiaAtual.StRu - varDiaAtual.Etr, 0)
            varDiaAtual.EtrEtm = 100 * varDiaAtual.Etr / varDiaAtual.Etm

            return varDiaAtual

        def posColheita(diaAtual, varDiaAnterior):
            varDiaAtual = VariaveisBalHidrico(self.parametros)

            varDiaAtual.ETP = self.calcularETP(diaAtual)
            varDiaAtual.Hr = 0
            varDiaAtual.Kc = 1

            varDiaAtual.Esc = self.calcularEsc(diaAtual)
            varDiaAtual.Apport = self.calcularApport(diaAtual, varDiaAtual.Esc)

            varDiaAtual.Etm = self.calcularEps(diaAtual, varDiaAtual.ETP)
            varDiaAtual.Epc = 0

            varDiaAtual.StRuSurf = min(varDiaAnterior.StRuSurf + varDiaAtual.Apport, self.parametros.RUSURF)
            varDiaAtual.Evs = min(varDiaAtual.Etm * varDiaAtual.StRuSurf / self.parametros.RUSURF, varDiaAtual.StRuSurf)
            varDiaAtual.Etr = varDiaAtual.Evs

            (varDiaAtual.StRu, varDiaAtual.Hum, varDiaAtual.Dr) = self.rempliRu(varDiaAtual.Apport,varDiaAnterior.StRu,
                                                                                varDiaAnterior.Hum)

            varDiaAtual.StRu = max(varDiaAtual.StRu - varDiaAtual.Etr, 0)
            varDiaAtual.StRuSurf = max(varDiaAtual.StRuSurf - varDiaAtual.Etr, 0)
            varDiaAtual.Eps = 0
            varDiaAtual.Vrad = 0
            varDiaAtual.StRur = varDiaAnterior.StRur
            varDiaAtual.StRurMax = varDiaAnterior.StRurMax
            varDiaAtual.TP = varDiaAnterior.TP
            varDiaAtual.EtrEtm = 100 * varDiaAtual.Etr / varDiaAtual.Etm

            return varDiaAtual

        self.parametros = parametros
        (self.dadosPrecipitacao, self.dadosTemperatura) = self.lerDadosPrecTemp()
        self.dadosIrrigacao = {x: 0 for x in self.dadosPrecipitacao}
        self.ETPsDecendiais = self.etp_Thornthwaite()

        diaAtual = self.parametros.inicioSimul

        varDiaAnterior = VariaveisBalHidrico(self.parametros)

        self.valoresDiarios = {}

        while diaAtual < self.parametros.inicioPlantio:
            varDiaAtual = preSemeio(diaAtual, varDiaAnterior)

            self.valoresDiarios[diaAtual] = varDiaAtual
            diaAtual += timedelta(days=1)
            varDiaAnterior = varDiaAtual

        while diaAtual <= self.parametros.diaColheita:
            varDiaAtual = fasesFenologicas(diaAtual, varDiaAnterior)

            self.valoresDiarios[diaAtual] = varDiaAtual
            diaAtual += timedelta(days=1)
            varDiaAnterior = varDiaAtual

        while diaAtual < self.parametros.fimSimul:
            varDiaAtual = posColheita(diaAtual, varDiaAnterior)

            self.valoresDiarios[diaAtual] = varDiaAtual
            diaAtual += timedelta(days=1)
            varDiaAnterior = varDiaAtual

        return self.valoresDiarios


