#
def tempo_restante_dia(hora, minutos):
    total_minutos = (hora * 60) + minutos
    total_dia = 24 * 60
    restante = total_dia - total_minutos

    return restante

#
hora = int(input('Qual a hora agora? '))
minutos = int(input('Qual os minutos agora? '))

#
totalminutos = (hora * 60) + minutos
hora2 = tempo_restante_dia(hora, minutos) // 60
minutos2 = tempo_restante_dia(hora, minutos) % 60

#
print(f'\nJá se passaram {totalminutos} minutos desde o início do dia.')
print(f'\nAinda faltam {tempo_restante_dia(hora, minutos)} minutos para o fim do dia.')
print(f'Ou {hora2} horas e {minutos2} minutos.')