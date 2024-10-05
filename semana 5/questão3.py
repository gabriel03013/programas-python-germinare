while True:
    n = int(input('Digite um número positivo inteiro: '))

    if n < 0:
        print('O número é negativo, portanto o programa vai encerrar.')
        break

    soma = 0
    impares = 0
    if n % 2 == 0:
        impares = n / 2
    else:
        impares = (n // 2) + 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            soma += i
    break


print(f'A soma dos números impares entre 1 e {n} é {soma}')
print(f'Entre 1 e {n}, há {impares:.0f} números ímpares.')
