from validate_docbr import CPF
import random
import datetime
cpf_validator = CPF()

#cores
class color:
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    NEGRITO = '\033[1m'
    SUBLINHADO = '\033[4m'
    NORMAL = '\033[0;0m'

#informações
print('\n')
nomecliente = input('Qual o nome do pagador? ')
agencia = int(input('Qual a Agência do pagador? '))
conta = input('Digite o número da conta corrente do pagador: ')

nomebeneficiario = input('\nQual o nome do beneficiário? ')
chave = input('Qual a chave do beneficiário? ')
cpfbeneficiario = input('Qual o CPF do beneficiário? (Sem pontos ou traço) ')
valor = float(input('Qual o valor que deseja transferir? '))

#
tracos = '-' * 20
id = random.randint(1000000, 9999999)

#ifs
if len(conta) != 7:
    print('CONTA CORRENTE INVÁLIDA')
else:
    contacorrente = conta

if len(cpfbeneficiario) != 11:
    print('CPF INVÁLIDO')
else:

#cpf
    if cpf_validator.validate(cpfbeneficiario):
        cpfformatado = cpf_validator.mask(cpfbeneficiario)
    else:
        print('CPF INVÁLIDO')

#data
dataatual = datetime.datetime.now().strftime("%d/%m/%Y")

#
print(f'{color.NEGRITO}{color.VERDE} \nDados do cliente {color.NORMAL}')
print(f'{color.NEGRITO}Nome:{color.NORMAL} {nomecliente}')
print(f'{color.NEGRITO}Agência:{color.NORMAL} {agencia:04}')
print(f'{color.NEGRITO}Conta corrente:{color.NORMAL} {contacorrente}')

print(f'\n{color.AZUL} {tracos}')

print(f'{color.NEGRITO}{color.VERDE}DADOS DA TRANSFERÊNCIA {color.NORMAL}')
print(f'{color.NEGRITO}Para:{color.NORMAL} {nomebeneficiario}')
print(f'{color.NEGRITO}Instituição:{color.NORMAL} Picpay')
print(f'{color.NEGRITO}Chave:{color.NORMAL} {chave}')
print(f'{color.NEGRITO}CPF:{color.NORMAL} {cpfformatado}')
#
if valor >= 1500:
    print(f'{color.AZUL}Valor: R$ {valor:.2f}{color.NORMAL}')
else:
    print(f'{color.VERMELHO}Valor: R$ {valor:.2f}{color.NORMAL}')
#
print(f'{color.AZUL} {tracos}')
#
print(f'{color.NEGRITO}{color.VERDE}ID/Transação {color.NORMAL}')
print(f'{color.NEGRITO}ID:{color.NORMAL} {id}')
print(f'{color.NEGRITO}Data:{color.NORMAL} {dataatual}')
print('\n')