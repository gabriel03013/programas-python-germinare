# informações
populacao_inicial = float(input("Digite a população inicial: "))
taxa_crescimento = float(input("Digite a taxa de crescimento anual (em decimal, 15% = 0,15): "))
anos = int(input("Digite o número de anos: "))
taxa_mortes = int(input('Digite a média de mortes anualmente:' ))

# calculo
total_mortes = taxa_mortes * anos
população_final = populacao_inicial * taxa_crescimento * anos - total_mortes

# resultado
print(f'A população final será de {população_final:.0f} habitantes')