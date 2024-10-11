def validar_email_usuario(email):
        if '@' in email and '.com.br' in email:
            return True
        else:
            return False
        

nome = input('\nDigite seu nome completo: ').title()
email = input('\nDigite seu email: ').lower()

#
if validar_email_usuario(email):
    print(f'\nO email de {nome} é válido!')
else:
    print(f'\nO email de {nome} é inválido!')