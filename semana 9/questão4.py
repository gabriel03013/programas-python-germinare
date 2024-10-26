print('Comparativo de Consumo de Combustível')

#
veiculos = []
litro = []

#
for c in range(1,6):
    print(f'Veículo {c}')
    carro = input('Nome: ')
    veiculos.append(carro)

    km = float(input('Km por litro: '))
    litro.append(km)

#
print('Relatório final:')

for i, carros_litros in enumerate(veiculos):
    print(f' {i + 1} - {veiculos[i]:<20}- {litro[i]:<5} - {(1000 / litro[i]):.1f} litros - R$ {((1000 / litro[i]) * 2.25):.2f}')

#
menor_consumo = 0
for j in range(len(veiculos)):
    if litro[j] > menor_consumo:
        menor_consumo = litro[j]
        carro_consumo = veiculos[j]

print(f'O carro com o menor consumo é o {carro_consumo}.')