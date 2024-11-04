clientes= {
    'Nome' : 'Ana Maria Braga',
    'Endereço' : 'Av. Maria Augusta, s/n',
    'Operadora Celular' : 'Vivo',
}

def procurar_cliente(clientes, pesquisa):
    clientes_encontrados = []
    for chave, valor in clientes.items():
        if pesquisa.lower() in valor.lower():
            clientes_encontrados.append((chave, valor))
    
    if clientes_encontrados:
        for nome, resultado in clientes_encontrados:
            print(f'{nome} : {resultado}')
    else:
        print('Nenhum cliente encontrado')

pesquisa = input('Por quem deseja pesquisar? ')
procurar_cliente(clientes, pesquisa)