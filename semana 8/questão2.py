from random import randint
idades = []

#
for i in range(80):
    idade_aleatoria = randint(1,100)
    idades.append(idade_aleatoria)

#
bebe = 0
crianca = 0
pre_adolescente = 0
adolescente = 0
jovem = 0
adulto = 0
idoso = 0

#
for idade in idades:
    if idade <= 2:
        bebe += 1
    elif 2 < idade <= 10:
        crianca += 1
    elif 10 < idade <= 14:
        pre_adolescente += 1
    elif 14 < idade <= 18:
        adolescente += 1
    elif 18 < idade <= 21:
        jovem += 1
    elif 21 < idade <= 60:
        adulto += 1
    elif idade > 60:
        idoso += 1

#
print(f'A média das idades é: {sum(idades) / len(idades):.0f}')
print(f'A maior idade é: {max(idades)}')
print(f'A menor idade é: {min(idades)}')

#
print(f'\nBebês: {bebe}\nCrianças: {crianca}\nPré adolescentes: {pre_adolescente}\nAdolescentes: {adolescente}\nJovens: {jovem}\nAdulto: {adulto}\nIdosos: {idoso}')
