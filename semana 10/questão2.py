conta = {'Transações': 0, 'Saldo': 1000, 'Média': 0}

def compra(conta, valor):
    conta.update({'Transações': conta['Transações'] + 1})  
    conta.update({'Saldo': conta['Saldo'] - valor})
    conta.update({'Média': ((conta['Média'] + valor) / conta['Transações'])})
   
    return conta

while True:
    valor = float(input('Digite o valor da compra que deseja efetuar: '))

    if valor > conta['Saldo']:
        print('Saldo insuficiente\nSaindo...')
        break

    compra(conta,valor)

    continuar = input('Deseja comprar mais algo? (S / N) ').upper()

    if continuar != 'S':
        print('Saindo...')
        break

print(conta)