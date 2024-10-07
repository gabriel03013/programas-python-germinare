from random import randint

#
saldo = 100

#
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
NEGRITO = '\033[1m'
SUBLINHADO =' \033[4m'
NORMAL = '\033[0;0m'

#
while saldo > 0:
    aposta = int(input(f'\n{AZUL}{NEGRITO}Você tem um saldo restante de {saldo}, quanto deseja apostar? {NORMAL}'))
    
    #
    if aposta > saldo:
        print(f'{VERMELHO}Você deve fazer uma aposta dentro do limite do seu saldo restante! {NORMAL} ')
    else:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        soma_dados = dado1 + dado2
        print(f'{AMARELO}Os dados foram girados...{NORMAL}')
        
        #
        if soma_dados == 7 or soma_dados == 11:
            ganho = aposta * 2
            saldo += ganho
            print(f'\n{VERDE}Parabéns sortudo! Sua aposta foi dobrada e seu saldo atualizado!{NORMAL} ')

        else:
            saldo -= 20
            print(f'\n{VERMELHO}Que pena, você foi azarado dessa vez! Você perdeu 20 pontos no seu saldo.{VERMELHO}')

#
print(f'\n{VERMELHO}{NEGRITO}Seus pontos se esgotaram :( {NORMAL } ')



