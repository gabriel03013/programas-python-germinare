pessoas = {

}

def incluir_nome_telefone(nome, telefone):
    pessoas[nome] = {'telefone1': telefone}

def incluir_telefone(nome, novo_telefone, telefone):
    if nome in pessoas:
        pessoas[nome][novo_telefone] = telefone

def excluirTelefone(nome, telefone):
    if nome in pessoas:
        for chave, valor in pessoas[nome].items():
            if valor == telefone:
                pessoas[nome].pop(chave)
                print('Telefone excluído.')
                return
        print('Telefone não encontrado.')
    
    else:
        print('Contato não encontrado.')

def excluirTelefone(nome, telefone):
    if nome in pessoas:
        for key, value in pessoas[nome].items():
            if value == telefone:
                pessoas[nome].pop(key)
                print('Telefone excluído.')

                if not pessoas[nome]:
                    del pessoas[nome]
                    print('O contato foi excluído por havia apenas um telefone.')
                
                return
        
        print('Telefone não encontrado.')
    else:
        print('Contato não encontrado.')

def excluirNome(nome):
    if nome in pessoas:
        del pessoas[nome]
        print('Contato excluído.')
    else:
        print('Contato não encontrado.')

print('1 - Incluir nome e telefone\n2 - Incluir telefone em um nome\n3 - Excluir telefone\n4 - Excluir contato')
while True:
    opcao = int(input('Digite sua opção: '))
    nome = input('Digite um nome: ').title()
    
    if opcao == 1:
        telefone = input('Digite o telefone para o contato: ')
        incluir_nome_telefone(nome, telefone)
        print('Contato adicionado.')

    elif opcao == 2:
        if nome in pessoas:
            novo_telefone = input('Esse vai ser o telefone 1, 2, 3 ou mais? ')
            telefone = input('Digite o novo telefone: ')
            incluir_telefone(nome, f'telefone{novo_telefone}', telefone)
            print('Novo telefone adicionado.')
        else:
            telefone = input('Digite o telefone para o novo contato: ')
            print('Parece que o contato ainda não existe na lista de contatos, ele será adicionado.')
            incluir_nome_telefone(nome, telefone)
            print('Contato adicionado.')

    elif opcao == 3:
        telefone = input('Digite o telefone a ser excluído: ')
        excluirTelefone(nome, telefone)

    elif opcao == 4:
        excluirNome(nome)
    
    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar != 'S':
        break


print(f'Lista de contatos:\n')
for i  in pessoas.items():
    print(f'{i}')
