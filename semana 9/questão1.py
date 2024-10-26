#
contagem_salarios = [0] * 9
semanas = []
vendas_brutas = []

#
while True:
    semanas_trabalhadas = int(input('Quantas semanas o funcionário trabalhou? '))
    semanas.append(semanas_trabalhadas)

    venda_bruta = float(input('Quanto o vendedor vendeu em valor bruto? '))
    vendas_brutas.append(venda_bruta)

    continuar = str(input('Deseja continuar com os funcionários? '))
    if continuar in 'Nn':
        break

#
for vendas in vendas_brutas:
    for sm in semanas:
        salario = (sm * 200) + (0.09 * vendas)
    posicao = min(int((salario - 200) // 100), 8)
    contagem_salarios[posicao] += 1

#
intervalos = [
    "$200 - $299",
    "$300 - $399",
    "$400 - $499",
    "$500 - $599",
    "$600 - $699",
    "$700 - $799",
    "$800 - $899",
    "$900 - $999",
    "$1000 e acima"
]

#
print("Contagem de vendedores por faixa salarial:")
for i in range(len(contagem_salarios)):
    print(f"{intervalos[i]}: {contagem_salarios[i]}")