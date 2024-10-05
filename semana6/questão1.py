palavra = input('Digite uma palavra: ')

reverso = palavra[::-1]

vogais = 'aeiouAEIOU'

minusculo = palavra.lower()
nvogais = minusculo.count('a') + minusculo.count('e') + minusculo.count('i') + minusculo.count('o') + minusculo.count('u') 


print(f'A palavra: {palavra} de trás para frente é: {reverso}.')
print(f'A palavra: {palavra} possui {nvogais} vogais.')