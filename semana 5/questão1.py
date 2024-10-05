from datetime import date

#
data_atual = date.today()
dt = data_atual.year

#
while True:
    salario_inicial = float(input('Digite seu salário inicial: '))
    if salario_inicial < 1000:
        print('\nVocê não pode consultar seu aumento salarial. Seu salário inicial deve ser de pelo menos R$ 1000,00')
        break
    else: 
        print('\nAumento disponível! ')
    ano = int(input('\nDigite o ano em que você foi contratado pela JBS: '))
    if ano < 1995:
        print('Você não pode consultar seu aumento salarial.')
        break
    
    
    data = dt - ano
    
    #
    porcentagem_inicial = 1.5
    salario_final = salario_inicial
    porcentagemtotal = 0
    for i in range(data):
        salario_final = salario_final + (salario_final * porcentagem_inicial / 100)
        porcentagemtotal += porcentagem_inicial
        porcentagem_inicial += porcentagem_inicial * 0.1
    break

#
print(f'Seu salário final, com um aumento de {porcentagemtotal:.2f}%, será de : R$ {salario_final:.2f}')
