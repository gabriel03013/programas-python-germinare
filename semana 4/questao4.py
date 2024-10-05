nome1 = input('Digite seu nome: ')
nome2 = input('Digite o nome do(a) acompanhante: ')

idadep1 = int(input('Qual sua idade? '))
idadep2 = int(input('Qual a idade do(a) acompanhante? '))

#pessoa 1
if idadep1 <= 17:
    pessoa1 = 15
elif 18 <= idadep1 <= 59:
    pessoa1 = 30
else:
    pessoa1 = 20


#pessoa2
if idadep2 <= 17:
    pessoa2 = 15
elif 18 <= idadep2 <= 59:
    pessoa2 = 30
else:
    pessoa2 = 20

#
totalingressos = pessoa1 + pessoa2

#
print(f'\nPreço unitário de {nome1}: R$ {pessoa1:.2f}')
print(f'Preço unitario de {nome2}: R$ {pessoa2:.2f}')
print(f'\nO total dos dois ingressos é de: R$ {totalingressos:.2f}')

