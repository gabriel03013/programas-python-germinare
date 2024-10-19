#
valor_casa = float(input('Digite o valor total da casa: R$ '))
investimento = float(input('Digite o valor do investimento mensal para a compra da casa: R$ '))
juros = float(input('Digite a taxa mensal de juros (15% = 0.15): '))

#
if investimento < (valor_casa * 0.01):
    print('O valor do investimento é baixo demais (menor que 1% do valor da casa).')
else:
    #
    valor_atual = 0
    meses = 0

    #
    while valor_atual < valor_casa:
        valor_atual = valor_atual * (1 + juros) + investimento
        meses += 1

    #
    print(f'Serão necessários aproximadamente {meses} meses para comprar o imóvel.')
    print(f'Ou aproximadamente {(meses / 12):.1f} anos.')