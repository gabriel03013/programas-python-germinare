# informações sobre o funcionário
N = input('Qual seu nome? ')
H = int(input('Quantas horas ' + N + ' trabalha semanalmente? '))
D = int(input('Quantos dependentes ' + N +  ' tem? '))

# cálculo do salário
s1 = H * 25
salário_mensal = s1 * 4 + D * 500

# exibição do salário
print(f'{N} terá um salário mensal de R$ {salário_mensal:.2f}')