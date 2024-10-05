import math

AZUL = '\033[94m'
NORMAL = '\033[0;0m'
setinha = '-' * 10
setinha2 = '-' * 50
#
print(f'{AZUL}{setinha} BANCO ORIGINAL {setinha}{NORMAL}')

print(f'')
#
divida = float(input('Digite o valor da dívida: '))
if divida < 0:
    print('ERRO')
divida1 = divida
valormensal = float(input('Digite o valor que deseja pagar mensalmente: '))
meses = divida / valormensal
meses = math.ceil(meses)
mes = 1
#
while divida > 0:
    if valormensal < 0:
        break
    print(f'\nMês {mes} - Dívida antes do pagamento: R$ {divida:.2f}')
    print(f'{AZUL}{setinha2}{NORMAL}')
    divida -= valormensal
    if divida < 0:
        print('A sua dívida foi paga!')
        break
    
    print(f'Dívida após o pagamento: R$ {divida:.2f}')
    print(f'{AZUL}{setinha2}{NORMAL}')
    mes += 1