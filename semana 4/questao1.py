#
valor = int(input('Qual o valor que deseja sacar? '))

#
if valor < 10:
    erro = 'O valor mínimo de saque é de R$ 10'
    print(f'{erro}')
elif valor > 600:
    erro = 'O valor máximo de saque é de R$ 600'
    print(f'{erro}')
else:
    valor_original = valor

#
cem = valor // 100
valor = valor % 100

cinq = valor // 50
valor = valor % 50

dez = valor // 10
valor = valor % 10

cinco = valor // 5
valor = valor % 5

dois = valor // 2
valor = valor % 2

#
print(f'Para sacar a quantia de R$ {valor_original:.2f}, serão necessárias:')
print(f'{cem} nota(s) de R$ 100')
print(f'{cinq} nota(s) de R$ 50')
print(f'{dez} nota(s) de R$ 10')
print(f'{cinco} nota(s) de R$ 5')
print(f'{dois} nota(s) de R$ 2')