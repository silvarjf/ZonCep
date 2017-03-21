import csv, datetime, sqlite3



class Estacao():
    def __init__(self):
        self.keys = ['data', 'tmin', 'tminEst', 'tmed', 'tmedEst',
                'tmax', 'tmaxEst', 'urMin', 'urMinEst',
                'urMax', 'urMaxEst', 'prec', 'precEst']

        # self.dados = 'dados/AC/AC_Cruzeiro do Sul_9000204.csv'
        self.dados = 'dados/SP/SP_Campinas_9001125.csv'


    def lerDadosPrecTemp(self, dataInicial, dataFinal = None):
        if dataFinal is None:
            dataFinal = dataInicial

        precipitacao = {}
        temperatura = {}

        with open(self.dados) as arquivoDados:
            reader = csv.DictReader(arquivoDados, self.keys, delimiter=';')
            cabecalho = True
            data = None

            for linha in reader:
                if cabecalho is False:
                    if data is None:
                        data = str(linha['data']).rstrip().lstrip()
                        dia = int(data[:2])
                        mes = int(data[3:5])
                        ano = int(data[6:])
                        data = datetime.date(ano, mes, dia)
                    else:
                        data = data - datetime.timedelta(days=1)

                    if data <= dataFinal and data >= dataInicial:
                        precipitacao[data] = None if linha['prec'] == '' else float(linha['prec'].replace(',','.'))
                        temperatura[data] = None if linha['tmed'] == '' else float(linha['tmed'].replace(',', '.'))

                    elif data < dataInicial:
                        break


                else:
                    if str(linha['data']).rstrip(' ') == 'data':
                        cabecalho = False

            return (precipitacao, temperatura)



estacao = Estacao()

