pizza_menu = ['Mussarela', 'Calabresa', 'Frango com Catupiry']
tamanho_menu = ['Pequena', 'Média', 'Grande']
pizza_cliente = []
tamanho_cliente = []
c = 0

while True:
    print('\nMenu: \n1. Escolher sabor de pizza\n2. Escolher tamanho da pizza\n3. Adicionar refrigerante\n4. Finalizar pedido')
    opcao = int(input('\nEscolha uma opção: '))

    refrigerante = False

    if opcao == 1:
        print('\nOpções de sabores de pizza:')

        for pizzas in pizza_menu:
            c += 1
            print(f'{c}. {pizzas}')
        
        c -= 3
        
        escolha_pizza = int(input('Escolha um sabor (1/2/3): '))
        pizza_cliente.append(pizza_menu[escolha_pizza - 1])
        continue
    
    elif opcao == 2:
        print('\nOpções de tamanho de pizza: ')
        for tamanhos in tamanho_menu:
            c += 1
            print(f'{c}. {tamanhos}')
               
        escolha_tamanho = int(input('Escolha o tamanho: '))
        tamanho_cliente.append(tamanho_menu[escolha_tamanho - 1])
    elif opcao == 3:
        refrigerante = input('Deseja adicionar refrigerante? (S / N) ').capitalize()
        if refrigerante != 'S':
            refrigerante = False
        else:
            refrigerante = True
    
    elif opcao == 4:
        print('Saindo...')
        break

    else:
        print('Opção inválida, tente novamente.')
        continue

if len(pizza_cliente) != 0 or len(pizza_menu) != 0:
    print(f'Sabor(es) de pizza: {', '.join(pizza_cliente)}\b')
    print(f'Tamanho(s) da(s) pizza(s), respectivamente: {', '.join(tamanho_cliente)}\b')

    if refrigerante == False:
        print('Refrigerante não adicionado ao pedido.')
    else:
        print('Refrigerante não adicionado ao pedido.')

if len(pizza_cliente) != len(tamanho_cliente) or len(tamanho_cliente) != len(pizza_cliente):
    print('Pedido incompleto.')

else:
    print('Você não fez nenhum pedido.')