print('Mercado J&F - Promoção FRIBOI')

#
print('1- Filé Duplo')
print('2- Alcatra')
print('3- Picanha')

#
opcao = int(input('Digite o tipo que deseja levar: '))
quantidade = float(input('Digite a quantidade que deseja comprar (em Kg): '))
print('A compra será realizada em cartão de débito (desconto de 5%)? ')
print('1- SIM')
print('2- NÃO')
debito = int(input('Sua escolha: '))

#
if opcao == 1 and quantidade <= 5:
   valor1 = 4.90 * quantidade
elif opcao == 1 and quantidade > 5:
  valor1 =  5.80 * quantidade
elif opcao == 2 and quantidade <= 5:
   valor1 = 5.90 * quantidade
elif opcao == 2 and quantidade > 5:
   valor1 = 6.80 * quantidade
elif opcao == 3 and quantidade <= 5:
   valor1 = 6.90 * quantidade
elif opcao == 3 and quantidade > 5:
   valor1 = 7.80 * quantidade

#
print('\n*****CUPOM FISCAL*****')
if opcao == 1:
    print('* Carne: Filé Duplo')
elif opcao == 2:
   print('* Carne: Alcatra')
elif opcao == 3:
   print('* Carne: Picanha')

print(f'* Quantidade: {quantidade}Kg')
print(f'* Preço: R$ {valor1:.2f}')

if debito == 1:
   valor2 = valor1 * 0.05
   valortotal = valor1 - valor2
   print(f'* Cartão com Débito: SIM')
   print(f'* Total com desconto: R$ {valortotal:.2f}')
else:
   print(f'* Cartão com Débito: NÃO')
   print(f'* Total com desconto: R$ {valor1:.2f}')

final = '*' * 23
print(final)
