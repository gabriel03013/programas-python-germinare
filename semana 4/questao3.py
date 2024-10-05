#
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite mais outro número inteiro: '))

#
menor = num1
maior = num1
intermediario = num1

#
if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        intermediario = num2
        menor = num3
    else:
        intermediario = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        intermediario = num1
        menor = num3
    else:
        intermediario = num3
        menor = num1
elif num3 > num2 and num3 > num1:
    maior = num3
    if num2 > num1:
        intermediario = num2
        menor = num1
    else:
        intermediario = num1
        menor = num2

#
print(f'O maior número é {maior} e o menor é {menor}.')
print(f'A ordem crescente dos números é: {menor}, {intermediario}, {maior}.')
