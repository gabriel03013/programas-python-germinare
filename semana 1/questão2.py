import math

# informações
A = float(input('Qual é a altura do quintal? '))
L = float(input('Qual é a largura do quintal? '))
P = float(input('Qual é o preço da lata de tinta? '))

# cálculos
area_retangulo = A * L
litros_tinta = area_retangulo / 3
latas_tinta = math.ceil(litros_tinta / 5)
preço_lata = P * latas_tinta

# resultados
print(f'Você precisará de: {latas_tinta} latas de tinta')
print(f'Você precisará gastar: R$ {preço_lata:.2f}')