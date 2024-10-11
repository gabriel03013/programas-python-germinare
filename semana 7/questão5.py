#
def valor_arrecadado(telheiro, quadrado):
    t = telheiro * 1.05
    q = quadrado * 0.51
    total = t + q

    return total

#
def valor_comissão(total):
    comissao = total * 0.1

    return comissao

#
telheiro = float(input('Digite a quantidade de pregos telheiros que foram vendidos hoje: '))
quadrado = float(input('Digite a quantidade de pregos quadrado que foram vendidos hoje: '))

#
total = valor_arrecadado(telheiro, quadrado)

#
print(f'\nO valor arrecadado com as vendas de hoje foi de: R$ {valor_arrecadado(telheiro, quadrado):.2f}')
print(f'\nO valor que deve ser retornado como comissão é de: R$ {valor_comissão(total):.2f}')