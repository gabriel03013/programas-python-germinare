import math
from random import randint

def fatorial():
    a = randint(0,20)
    b = randint(0,20)
    
    soma = math.factorial(a) + math.factorial(b)

    print(f'Números gerados: {a} e {b}')

    return soma

print(f'A soma dos fatoriais é: {fatorial()} ') 