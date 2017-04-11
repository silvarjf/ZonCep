import sqlite3
from estacao import Estacao
from cultura import Cultura
from estrutura import ParamSimul
from balancoHidrico import balancoHidrico


estado = 'SE'
parametros = ParamSimul()

# Selecionar cultura
cultura = Cultura()
cultura.carregarDoBD(1)

# Selecionar todos as estações de um estado
conn = sqlite3.connect('sarra.db')
cursor = conn.cursor()

cursor.execute('''
SELECT estacao.codigo, estacao.nome, estacao.latitude, estacao.longitude,
estacao.altitude, estacao.municipio, municipio.nome, municipio.estado, estado.nome, estacao.dados
FROM estacao, municipio, estado
WHERE municipio.codigo = estacao.municipio AND municipio.estado = estado.sigla AND estado.sigla = "%s"''' % (estado))

estacoes = []

for linha in cursor.fetchall():
    estacoes.append(Estacao(cursorSQL=linha))

valoresDiarios = {}

nEstacoes = len(estacoes)
n = 1
for estacao in estacoes:
    print(estacao.nome + ': ' + str(n) + ' de ' + str(nEstacoes))
    simulacao = balancoHidrico(estacao, cultura)
    valoresDiarios[estacao.codigo] = simulacao.simularBalancoHidrico(parametros)
    n+=1

a = 1
