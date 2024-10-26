def filtragem():
    clientes_filtrados = []
    for cliente in clientes:
        nome, idade, cidade, gasto = cliente
        if idade_min <= idade <= idade_max and cidade == loc and gasto >= valor_min:
            clientes_filtrados.append(cliente)

    return clientes_filtrados

clientes = [
    ('Alice', 30, 'São Paulo', 500),
    ('Bob', 25, 'Rio de Janeiro', 300),
    ('Carol', 35, 'São Paulo', 700),
    ('David', 40, 'Brasília', 1000),
    ('Eva', 28, 'Rio de Janeiro', 400),
]

#

idade_min = int(input('Qual idade mínima deseja filtrar? '))
idade_max = int(input('Qual idade máxima deseja filtrar? '))

#
localizações_filtradas = []
loc = str(input('\nDigite a cidade que deseja filtrar: '))

#
gastos_filtrados = []
valor_min = float(input('\nDigite o valor mínimo gasto que deseja filtrar: '))

#
print(f'\nClientes filtrados: {filtragem()}')