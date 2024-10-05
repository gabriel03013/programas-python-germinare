while True:
    n = int(input('Digite um número inteiro positivo: '))
    #
    if n < 0:
        print('Digite um número positivo')
        break

    #
    if n % 2 == 0:
        eh_par_impar = f'O número {n} é par.'
    else:
        eh_par_impar = f'O número {n} é ímpar.'
    
    #
    divisoes = 0
    for i in range(1, n+ 1):
        if n % i == 0:
            divisoes += 1
        else:
            divisoes = divisoes
        
        if divisoes <= 2:
            eh_primo = f'{n} é um número primo.'
        else:
            eh_primo = f'{n} não é um número primo.'


    #
    if str(n) == str(n)[::-1]:
        eh_palindromo = 'O número é um palíndromo.'
    else:
        eh_palindromo = 'O número não é um palíndromo.'

    #
    if n ** 0.5 == int(n ** 0.5):
        eh_quadradoPerfeito = f'O número {n} é um quadrado perfeito.'
    else:
        eh_quadradoPerfeito = f'O número {n} não é um quadrado perfeito.'
    
    #
    soma = 0
    numdigitos = len(str(n))

    for d in str(n):
        soma += int(d) ** numdigitos
        if soma == n:
            eh_armstrong = f'{n} é um número de armstrong.'
        else:
            eh_armstrong = f'{n} não é um número de armstrong.'
    
    #
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    if a == n:
        tem_fibonacci = 'O número faz parte da sequência de fibonacci.'
    else:
        tem_fibonacci = 'O número não faz parte da sequência de fibonacci.'

    break

#
print(f'\n{eh_par_impar}')
print(f'\n{eh_primo}')
print(f'\n{eh_palindromo}')
print(f'\n{eh_armstrong}')
print(f'\n{tem_fibonacci}')
