import random

# questão 1
acertos = 0
n1 = random.randint(1,20)
n2 = random.randint(1,20)
r1 = n1 * n2
p1 = int(input(f'Pergunta 1: {n1} x {n2} = '))
if p1 == r1:
    print('Acertou')
    acertos1 = acertos + 1
    print(f'Acertos atuais: {acertos1}')
else:
    print('Errou')
    acertos1 = acertos + 0
    print(f'Acertos atuais: {acertos1}')

#questão 2
n3 = random.randint(1,20)
n4 = random.randint(1,20)
r2 = n3 * n4
p2 = int(input(f'Pergunta 2: {n3} x {n4} = '))
if p2 == r2:
    print('Acertou')
    acertos2 = acertos1 + 1
    print(f'Acertos atuais: {acertos2}')
else:
    print('Errou')
    acertos2 = acertos1 + 0
    print(f'Acertos atuais: {acertos2}')

#questão 3
n5 = random.randint(1,20)
n6 = random.randint(1,20)
r3 = n5 * n6
p3 = int(input(f'Pergunta 3: {n5} x {n6} = '))
if p1 == r1:
    print('Acertou')
    acertos3 = acertos2 + 1
    print(f'Acertos atuais: {acertos3}')
else:
    print('Errou')
    acertos3 = acertos2 + 0
    print(f'Acertos atuais: {acertos3}')

#questão 4
n7 = random.randint(1,20)
n8 = random.randint(1,20)
r4 = n7 * n8
p4 = int(input(f'Pergunta 4: {n7} x {n8} = '))
if p4 == r4:
    print('Acertou')
    acertos4 = acertos3 + 1
    print(f'Acertos atuais: {acertos4}')
else:
    print('Errou')
    acertos4 = acertos3 + 0
    print(f'Acertos atuais: {acertos4}')

#questão 5
n9 = random.randint(1,20)
n10 = random.randint(1,20)
r5 = n9 * n10
p5 = int(input(f'Pergunta 5: {n9} x {n10} = '))
if p5 == r5:
    print('Acertou')
    acertos5 = acertos4 + 1
    print(f'Acertos atuais: {acertos5}')
else:
    print('Errou')
    acertos5 = acertos4 + 0
    print(f'Acertos atuais: {acertos5}')

#total
print(f'Você acertou {acertos5} questões!')
if acertos5 >=3:
    print('Parabéns! Continue assim!')

elif acertos5 <=2:
    print('Você pode melhorar!')