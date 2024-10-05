# informações
h = int(input('Quantas horas deseja converter para segundos?(apenas o número cru, tipo 1, ou 2...) ' ))
m = int(input('Quantas minutos deseja converter para segundos?(apenas o número cru, tipo 10, ou 20...)' ))
s = int(input('Quantos segundos restam?(apenas o número cru, tipo 50, 40...)'  ))

# calculos
horas = h * 3600
minutos = m * 60
segundos = horas + minutos + s

# resultado
print(f'{h}h {m}min {s}s resultará em {segundos} segundos')


