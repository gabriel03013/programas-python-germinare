import time

#
min = int(input('Qual o minuto inicial? '))
seg = min * 60

#
if min < 0:
    print('ERRO')

#
elif min == 0:
    seg = int(input('Quantos segundos então? '))
    if  60 >= seg > 0:
        for i in range(seg + 1):
            print(f'{seg:02}')
            seg -= 1
            time.sleep(1)
        print('FIM')

#
else:
    for i in range(seg, -1, -1):
        minutos_restantes = i // 60
        segundos_restantes = i % 60
        print(f'{minutos_restantes:02d}:{segundos_restantes:02d}')
        time.sleep(1)
    print('FIM')