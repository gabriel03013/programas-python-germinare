from datetime import datetime

#
def calcular_diferenca_idade(data1, data2):
    data1 = datetime.strptime(data1, '%Y-%m-%d')
    data2 = datetime.strptime(data2, '%Y-%m-%d')
     
    #
    if data2 > data1:
        data2,data1 = data1, data2
    
    #
    anos = data1.year - data2.year
    meses = data1.month - data2.month
    dias = data1.day - data2.day

    #
    if dias < 0:
        meses -= 1
        dias += (data1 - datetime(data1.year, data1.month, 1)).days

    #    
    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

data1 = input('Digite a data de nascimento da Pessoa 1 (ano-mes-dia): ')
data2 = input('Digite a data de nascimento da Pessoa 2 (ano-mes-dia): ')

anos, meses, dias = calcular_diferenca_idade(data1, data2)

print(f'\nA diferença de idade entre as duas pessoas é de {anos} anos, {meses} meses e {dias} dias.')