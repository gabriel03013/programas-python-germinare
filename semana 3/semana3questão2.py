#informações
valor = float(input('Quanto você deseja pegar emprestado? '))
renda = float(input('Qual sua renda mensal atual? '))

print('\nResponda com SIM ou NÃO')

score = (input('\nSeu score é acima de 450 pontos? '))       
divida = (input('Você não possui dividas ativas? '))                    
fb = (input('Você é funcionário publico? '))
ob = (input('Você aceita compartilhar seus dados de outros bancos pelo open banking? '))

#
respostas = [score, divida, fb, ob]
totalsim = respostas.count('SIM')

if renda >= valor * 2:
    print('Renda suficiente, sua renda tem o dobro do valor solicitado.')
    totalsim += 1
    print(f'Sua pontuação foi de {totalsim}')
else:
    print('Renda Insuficiente, sua renda tem que ser o dobro do valor solicitado para ter uma aprovação total.')
    print(f'Sua pontuação foi de {totalsim}')


#aprovações
valor_restricao = (20 / 100) * valor
valor_desconto = (60 / 100) * valor
aprovacaototal = valor

if totalsim == 2:
    print(f'Aprovado com Restrições, valor aprovado de R${valor_restricao:.2f}')

elif 3 <= totalsim <= 4:
    print(f'Aprovado com Desconto, valor aprovado de R${valor_desconto:.2f}')
    
elif totalsim == 5:
    print(f'Valor total aprovado, sendo R$ {aprovacaototal:.2f}')

else:
    print('Não Aprovado.')