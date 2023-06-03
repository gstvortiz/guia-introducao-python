#   Com as tuplas dos 20 primeiros colocados da Liga Juvenil de Futebol Amador,
#   ordenados de acordo com sua colocação, escreva na tela:
#       print('Os 5 primeiros times.
#       print('Os últimos 4 colocados.
#       print('Times em ordem alfabética.
#       print('Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoence', 'CSA', 'Avaí')

print('Os 5 primeiros times são:', times[:5])
print('Os últimos 4 colocados são:', times[-4:])
print('Times em ordem alfabética:', sorted(times))
print('Em que posição está o time da Chapecoense:', times.index('Chapecoence') + 1)