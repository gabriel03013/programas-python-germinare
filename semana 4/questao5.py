total = 0

#
tempo = int(input('Qual foi o tempo em minutos de conclusão da prova pelo candidato? '))
idade = int(input('Qual a idade do participante? '))
genero = input('Qual o gênero do candidato? (Masculino ou Feminino) ')
#
corrida = input('Qual o tipo de corrida? (Trilha/Asfalto/Híbrida) ')

if corrida == 'Híbrida':
    km_trilha = float(input('Quantos quilômetros o participante percorreu em trilha? '))

#
recorde = input('O participante quebrou algum recorde? (Sim ou Não) ')
if recorde == 'Sim':
    qtrecorde = int(input('Quantos recordes? '))
    total += qtrecorde * 50
else:
    total += 0
#
infracoes = input('O candidato cometeu alguma infração? (Sim ou Não)')


#tempo
if tempo < 30:
    pontostempo = 100
elif 30 <= tempo <= 60: 
    pontostempo = 100 - (tempo - 30)
elif 60 < tempo <= 90:
    pontostempo = 70 - (tempo - 60)
else:
    pontostempo = 40

#idade
if idade < 18:
    pontosidade = 20
elif 18 <= idade <= 30:
    pontosidade = 10
elif 30 > idade <= 45:
    pontosidade = 15
elif 45 > idade <= 60:
    pontosidade = 20
else:
    pontosidade = 25

#genero
if genero == 'Feminino':
    pontosgenero = 5
else:
    pontosgenero = 0

total = pontosgenero + pontosidade + pontostempo


# infracoes
if infracoes == 'Sim':
    print('Qual infração o participante cometeu?')
    print('1 - Corte de caminho (-10 pontos)')
    print('2 - Recebimento de ajuda externa (Desqualificação)')
    tipoinf = int(input('Digite: '))
    if tipoinf == 1:
        total -= 10
    elif tipoinf == 2:
        pontuacaofinal = 'Desqualificado'
    else: 
        print('Seleção inválida.')

#corrida
if corrida == 'Trilha':
    pontostipo = total * 0.1
if corrida == 'Híbrida':
    pontostipo = total * (0.05 * km_trilha)
else:
    pontostipo = 0

#
if infracoes == 'Sim' and tipoinf == 2:
    print("O PARTICIPANTE FOI DESQUALIFICADO!")
elif recorde == 'Sim':
    pontuacaofinal = total + pontostipo + qtrecorde
    print(f"A pontuação final do participante é: {pontuacaofinal:.0f} pontos")
else:
    pontuacaofinal = total + pontostipo
    print(f"A pontuação final do participante é: {pontuacaofinal:.0f} pontos")