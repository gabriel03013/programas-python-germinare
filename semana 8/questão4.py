#
total_produtos = 0
numero_produto = 1
total_preço = 0

#
while True:
    print(f'\n-------Seja bem vindo a Swift !-------')
    print(f'Estamos com uma promoção imperdível nas compras acima de R$ 100,00 !\n4 produtos -> 4% de desconto\n5 produtos -> 8% de desconto\n6 ou mais produtos -> 12% de desconto')
    
    produtos = int(input('\nQuantos produtos deseja comprar? '))
    
    #
    for i in range(produtos):
        print('-' * 20)
        preço = float(input(f'Digite o preço do {numero_produto}° produto: '))
        total_preço += preço
        numero_produto += 1
        
        #
    if produtos == 4 and total_preço >= 100:
        preço_cdesconto = total_preço - (0.04 * total_preço)
        desconto = 4
        valor_desconto = 0.04 * total_preço
        
    elif produtos == 5 and total_preço >= 100:
        preço_cdesconto = total_preço - (0.08 * total_preço)
        desconto = 8
        valor_desconto = 0.08 * total_preço
        
    elif produtos >= 6 and total_preço >= 100:
        preço_cdesconto = total_preço - (0.12 * total_preço)
        desconto = 12
        valor_desconto = 0.12 * total_preço
        
    elif produtos == 1:
        preço_cdesconto = total_preço
        
    elif produtos < 1:
        print(f'Quantidade inválida.')
        break

    #
    print(f'\nO valor total da compra é de: R$ {total_preço:.2f}')
    print(f'Quantidade de produtos: {produtos}')
    print(f'O valor total da compra com desconto é de: R$ {preço_cdesconto:.2f}')
    #
    if produtos > 1 and total_preço >= 100:
        print(f'O percentual do desconto é de: {desconto:.2f}%')
        print(f'O valor do desconto é de: R$ {valor_desconto:.2f}') 
    else:
        print(f'Você não tem direito a nenhum desconto.')
    
    #
    continuar = input(f'Há algum outro cliente na loja? (Sim/Não)').capitalize()
    if continuar == 'Não':
        print(f'Fim dos clientes!')
        break
    elif continuar == 'Sim':
        '\n'
    else:
        print(f'Opção inválida!')
        break

    numero_produto -= (numero_produto - 1)
    total_preço -= total_preço