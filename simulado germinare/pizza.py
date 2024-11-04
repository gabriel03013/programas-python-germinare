def sabor_pizza(pizza, opcao):
    if 0 < opcao < len(pizza) + 1:
        sabor = f'O sabor que você escolheu foi: {pizza[opcao - 1]}'
    else:
        sabor = 'Sabor inválido'

    return sabor

pizza = ['Pizza de Mussarela','Pizza de Calabresa','Pizza de Calabresa c/ Requeijão','Pizza de Frango c/ Catupiry']

print('===== SABORES DE PIZZA =====\n-Pizza de Mussarela\n-Pizza de Calabresa\n-Pizza de Calabresa c/ Requeijão\n-Pizza de Frango c/ Catupiry')

while True:
    opcao = int(input('\nQual opção deseja escolher? '))

    sabor_pizza(pizza, opcao)

    continuar = str(input('Deseja pedir outro sabor? (Sim \ Não) ')).capitalize()

    if continuar == 'Sim':
        continue
    elif continuar == 'Não':
        print('Saindo...')
        break
    else:
        print('Opção inválida, saindo...')
        break