salario = float(input('Digite seu salário: R$ '))

def imposto_de_renda(salario):
    if salario <= 1900:
        imposto = 0
    elif salario > 1900 and salario < 2800:
        imposto = (salario * 12 * 0.075) - 142.80
    elif salario > 2800 and salario < 3800:
        imposto = (salario * 12 * 0.15) - 354.80
    elif salario > 3800 and salario < 4600:
        imposto = (salario * 12 * 0.225) - 636.13
    elif salario > 4600:
        imposto = (salario * 12 * 0.275) - 869.36
    else:
        'Salário inválido'
    
    return imposto

print(f'Você deve pagar R$ {(imposto_de_renda(salario)):.2f} de imposto.')
