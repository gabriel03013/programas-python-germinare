import math

#informações 
horaentrada = int(input('Digite a hora da entrada: '))
minutoentrada = int(input('Digite o minuto da entrada: '))
horasaida = int(input('Digite a hora da saída: '))
minutosaida = int(input('Digite o minuto da saída: '))

#
minsentrada = horaentrada * 60 + minutoentrada
minsaida = horasaida * 60 + minutosaida

#
if minsaida < minsentrada:
    minsaida += 24 * 60

#
totalminutos = minsaida - minsentrada
horasestacionadas = math.ceil(totalminutos / 60)

#
if horasestacionadas <= 2:
    preco = horasestacionadas * 1.00
elif horasestacionadas <= 4:
    preco = 2 * 1.00 + (horasestacionadas - 2) * 1.40
else:
    preco = 2 * 1.00 + 2 * 1.40 + (horasestacionadas - 4) * 2.00

#
print(f'O tempo estacionado foi de {horasestacionadas} horas.')
print(f'O preço a pagar é de R$ {preco:.2f}')