from random import randint

print('\nModos de jogo: \n1- Fácil \n2- Médio \n3- Difícil')

#
modo = int(input('Digite o modo que deseja jogar: '))
jog = 0
pc = 0
tentativas = 0

#
if modo == 1:
    while True:
        jog = int(input('Qual número entre 1 e 10 você acha que o computador está pensando? '))
        if jog > 0 and jog <= 10:
            pc = randint(1,10)
            if jog == pc:
                print('Parábens! Você acertou!')
                print(f'Você precisou de {tentativas} para advinhar o número.')
                continuar = input('Deseja continuar? (S/N) ').upper()
                if continuar == 'N':
                    break
            else:
                continuar1 = input(f'Poxa, você errou. O número era {pc} Deseja tentar novamente? (S/N) ').upper()
                '\n'
                tentativas += 1
                if continuar1 == 'N':
                    break
        else:
            print('Insira um número inteiro positivo maior que 0 e menor que 10.')
            '\n'

#
elif modo == 2:
    while True:
        jog = int(input('Qual número entre 1 e 50 você acha que o computador está pensando? '))
        if jog > 0 and jog <= 50:
            pc = randint(1,50)
            if jog == pc:
                print('Parábens! Você acertou!')
                print(f'Você precisou de {tentativas} para advinhar o número.')
                continuar = input('Deseja continuar? (S/N) ').upper()
                if continuar == 'N':
                    break
            else:
                continuar1 = input(f'Poxa, você errou. O número era {pc} Deseja tentar novamente? (S/N) ').upper()
                '\n'
                tentativas += 1
                if continuar1 == 'N':
                    break
        else:
            print('Insira um número inteiro positivo maior que 0 e menor que 50.')
            '\n'

#
elif modo == 3:
    while True:
        jog = int(input('Qual número entre 1 e 100 você acha que o computador está pensando? '))
        if jog > 0 and jog <= 100:
            pc = randint(1,100)
            if jog == pc:
                print('Parábens! Você acertou!')
                print(f'Você precisou de {tentativas} para advinhar o número.')
                continuar = input('Deseja continuar? (S/N) ').upper()
                if continuar == 'N':
                    break
            else:
                continuar1 = input(f'Poxa, você errou. O número era {pc} Deseja tentar novamente? (S/N) ').upper()
                '\n'
                tentativas += 1
                if continuar1 == 'N':
                    break
        else:
            print('Insira um número inteiro positivo maior que 0 e menor que 100.')
            '\n'
#
else:
    print('Insira uma escolha válida.')
    '\n'
