#
alunos_turma = int(input('Quantos alunos tem na turma? '))
nomes = []
lista_notas1 = []
lista_notas2 = []
medias = []
conceitos = []

#
for al in range(1, alunos_turma + 1):
    #
    nome = input(f'Digite o nome do {al}º aluno: ').title()
    nomes.append(nome)

    #
    nota1 = float(input(f'Digite a primeira nota de {nome}: '))
    lista_notas1.append(nota1)

    nota2 = float(input(f'Digite a segunda nota de {nome}: '))
    lista_notas2.append(nota2)

    #
    media = (nota1 + nota2) / 2
    medias.append(media)

    if media >= 7:
        conceito = 'Aprovado'
    else:
        conceito = 'Reprovado'
    conceitos.append(conceito)

#
print(f"\n{'N:':<10} {'Aluno:':<10} {'Nota 1:':<10} {'Nota 2:':<10} {'Média:':<10} {'Conceito:':<10}")
for i, n in enumerate(nomes):
     print(f"{i + 1:<10} {nomes[i]:<10} {lista_notas1[i]:<10.1f} {lista_notas2[i]:<10.1f} {medias[i]:<10.1f} {conceitos[i]:<10}")
    

#
print(f'\nAprovados: {conceitos.count("Aprovado")}')
print(f'Reprovados: {conceitos.count("Reprovado")}')

#
media_turma = (sum(lista_notas1) + sum(lista_notas2)) / (len(lista_notas1) + len(lista_notas2))
print(f'\nMédia da turma: {(sum(lista_notas1) + sum(lista_notas2)) / (len(lista_notas1) + len(lista_notas2)):.1f}')

for c, alunos_abaixo_media in enumerate(nomes):
    if medias[c] < media_turma:
        print(f'O(A) aluno(a) {nomes[c]} ficou com a média abaixo da média da turma.')