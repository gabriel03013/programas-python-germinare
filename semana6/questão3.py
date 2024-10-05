#
lucas = 0
wellington = 0
gabriella = 0
nulo = 0
total_alunos = 0
votos_invalidos = 0

#
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
NEGRITO = '\033[1m'
SUBLINHADO =' \033[4m'
NORMAL = '\033[0;0m'

#
while True:
    print(f'{NEGRITO}Em quem você deseja votar? \n\n{AZUL}[1] Lucas \n[2] Wellington \n[3] Gabriella{NORMAL} \n{NEGRITO}[0] Voto em branco(nulo){NORMAL}')
    voto = int(input(f'\n{NEGRITO}Digite sua escolha: {NORMAL}'))
    #
    if voto == 1:
        print(f'\n{VERDE}Você votou em Lucas.')
        lucas += 1
    elif voto == 2:
        print(f'\n{VERDE}Você votou em Wellington.')
        wellington += 1
    elif voto == 3:
        print(f'\n{VERDE}Você votou em Gabriella.')
        gabriella += 1
    elif voto == 0:
        print(f'{NEGRITO}Você votou nulo.')
        nulo += 1
    else:
        print(f'{VERMELHO}Voto não computado! Você não escolheu nenhum candidato e também não votou nulo.')
        votos_invalidos += 1
        total_alunos += 0
    #
    total_alunos += 1
    continuar = input(f'{NORMAL}{NEGRITO}\nDeseja continuar as votações? S/N ').upper()
    if continuar == 'S':
        print(f'{AMARELO}Próximo eleitor!{NORMAL}')
    elif continuar == 'N':
        print(f'{NEGRITO}{SUBLINHADO}{VERMELHO}-------Votações encerradas-------{NORMAL}')
        break
    else:
        print(f'{VERMELHO}Seleção inválida!{NORMAL}')

#
votos_validos = total_alunos - votos_invalidos
print(f'{NEGRITO}{SUBLINHADO}{total_alunos} pessoas votaram para a escolha do representante.')
print(f' {votos_validos} votos foram válidos.')
print(f' {nulo} pessoa(s) votaram nulo.')

#
if wellington < lucas > gabriella:
    porcentagem_ganhador = (lucas / votos_validos) * 100
    ganhador = 'Lucas'
    print(f'\nO candidato vencedor foi {ganhador}, com {porcentagem_ganhador:.2f}% dos votos!')

elif wellington < gabriella > lucas:
    porcentagem_ganhador = (gabriella / votos_validos) * 100
    ganhador = 'Gabriella'
    print(f'\nA candidata vencedora foi {ganhador}, com {porcentagem_ganhador:.2f}% dos votos!')

elif lucas == wellington or lucas == gabriella or gabriella == wellington:
    print(f'\n{VERMELHO}Houve empate, portanto haverá um segundo turno!')

else:
    porcentagem_ganhador = (wellington / votos_validos) * 100
    ganhador = 'Wellington'
    print(f'\nO candidato vencedor foi {ganhador}, com {porcentagem_ganhador:.2f}% dos votos!')