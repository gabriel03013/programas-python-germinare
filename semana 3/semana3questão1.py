#senha
senha = str(input('Digite sua senha (deve conter pelo menos 8 caracteres, uma letra maiúscula e uma minúscula, e algum desses simbolos: !,@,#,$,%) : ')).strip()

#
simbolos = '!@#$%'
numeros = '0123456789'

#verificação da senha
if len(senha) < 8:
    print('\nA senha deve conter pelo menos 8 caracteres.')
elif senha.islower():
    print('\nA senha deve conter pelo menos um caractere maiúsculo.')
elif senha.isupper():
    print('\nA senha deve conter pelo menos um carectere minúsculo')
elif any(s in senha for s in numeros):
    print('\nA senha não pode conter números.')
elif all(s not in senha for s in simbolos):
    print('\nA senha precisa conter algum dos símbolos citados.')
else:
    print('\nSenha válida!')

print('\n')