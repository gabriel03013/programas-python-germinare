def contar_letras(palavra):
    letras = {}
    for i in palavra:
        if i in letras:
            letras[i] += 1
        else:
            letras[i] = 1

    return letras

palavra = input('Digite uma palavra: ')
for letra, vezes in contar_letras(palavra).items():
    if vezes > 1:
        print(f'A letra {letra} aparece {vezes} vezes.')
    else:
        print(f'A letra {letra} aparece {vezes} vez.')