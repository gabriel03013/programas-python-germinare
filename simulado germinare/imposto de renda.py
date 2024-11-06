def calcular_imposto_renda(salario):
    if 1001 <= salario < 3001:
        imposto = salario * 0.1
    
    elif 3001 <= salario < 5001:
        imposto = salario * 0.2
    
    elif salario > 5001: 
        imposto = salario * 0.3

    return imposto

salario = float(input('Digite seu salário: '))

if salario < 1001:
    print('Você é isento de imposto de renda.')

else:
    print(f'O imposto de renda a ser pago é de: R$ {(calcular_imposto_renda(salario)):.2f}')