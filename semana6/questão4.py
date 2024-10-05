total_produtos = 0
numero_produto = 1
total_preço = 0
#
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
NEGRITO = '\033[1m'
SUBLINHADO =' \033[4m'
NORMAL = '\033[0;0m'
LARANJA = "\033[38;2;255;165;0m"

while True:
    print(f'\n{LARANJA}{NEGRITO}-------Seja bem vindo a Swift !-------{NORMAL}')
    print(f'{NEGRITO}Estamos com uma promoção imperdível nas compras acima de R$ 100,00 !\n5% de desconto em compras com 2 a 4 produtos\n10% de desconto em compras com 5 a 7 produtos\n15% nas compras acima de 8 produtos')
    
    produtos = int(input('\nQuantos produtos deseja comprar? '))
    
    #
    for i in range(produtos):
        print('-' * 20)
        preço = float(input(f'Digite o preço do {numero_produto}° produto: '))
        total_preço += preço
        numero_produto += 1
        
        #
    if 2 <= produtos <= 4 and total_preço > 100:
        preço_cdesconto = total_preço - (0.05 * total_preço)
        desconto = 5
        valor_desconto = 0.05 * total_preço
        
    elif 5 <= produtos <= 7 and total_preço > 100:
        preço_cdesconto = total_preço - (0.1 * total_preço)
        desconto = 10
        valor_desconto = 0.1 * total_preço
        
    elif produtos >= 8 and total_preço > 100:
        preço_cdesconto = total_preço - (0.15 * total_preço)
        desconto = 15
        valor_desconto = 0.15 * total_preço
        
    elif produtos == 1:
        preço_cdesconto = total_preço
        
    elif produtos < 1:
        print(f'{VERMELHO}Quantidade inválida.{NORMAL}')
        break

    else:
        preço_cdesconto = total_preço

    #
    print(f'{SUBLINHADO}\nO valor total da compra é de: R$ {total_preço:.2f}')
    print(f' Quantidade de produtos: {produtos}')
    print(f' O valor total da compra com desconto é de: R$ {preço_cdesconto:.2F}')
    #
    if produtos > 1 and total_preço > 100:
        print(f'{VERDE} O percentual do desconto é de: R$ {desconto:.2f}%{NORMAL}')
        print(f'{SUBLINHADO}O valor do desconto é de: R$ {valor_desconto:.2f}') 
    else:
        print(f'{VERMELHO} Você não tem direito a nenhum desconto.{NORMAL}')
    
    #
    continuar = input(f'{NEGRITO}Há algum outro cliente na loja? (Sim/Não){NORMAL} ').capitalize()
    if continuar == 'Não':
        print(f'{VERMELHO}Fim dos clientes!{NORMAL}')
        break
    elif continuar == 'Sim':
        '\n'
    else:
        print(f'{VERMELHO}Opção inválida!{NORMAL}')
        break

    numero_produto -= (numero_produto - 1)
    total_preço -= total_preço