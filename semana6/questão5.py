#
gabarito  = []
numero_questao = 1
notas = []
quantidade_alunos = 0

#
for i in range(1,11):
    resposta_pro = input(f'Digite a resposta da questão {numero_questao}: ').upper()
    numero_questao += 1
    gabarito.append(resposta_pro)

#
while True:
    numero_questaoalu = 1
    aluno = []
    nota = 0
    
    # 
    for c in range(1,11):
        resposta_aluno = input(f'Digite sua resposta da questão {numero_questaoalu}: ').upper()
        aluno.append(resposta_aluno)
        numero_questaoalu += 1
    
    #
    for alternativa in range(10):
        if aluno[alternativa] == gabarito[alternativa]:
            nota += 1  

    #
    quantidade_alunos += 1
    notas.append(nota)

    #
    print(f'A nota do aluno foi: {nota}')

    #
    continuar = input('Deseja continuar? S/N').upper()
    if continuar == 'N':
        break

#
media = (sum(notas)) / quantidade_alunos

#
print(f'{quantidade_alunos} alunos usaram o sistema para calcular sua nota.')
print(f'A media de notas da sala foi de: {media}')
print(f'A maior nota da sala foi {max(notas)}')