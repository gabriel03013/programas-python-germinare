# informações
segundos = int(input('Quantos segundos você deseja converter? '))

# cálculo
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes = segundos_restantes % 60

# resultado
print(f'\n{segundos} segundos resultará em {horas}h, {minutos}min, e {segundos_restantes}s.')