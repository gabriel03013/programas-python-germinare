#
via = int(input('Qual é a velocidade máxima permitida na via? '))
velocidade = int(input('Qual era a velocidade que o veículo estava na hora da infração? '))

#
infracao = velocidade - via

#
if velocidade <= via: 
    print('\nVelocidade dentro do limite! Portanto nenhuma multa foi aplicada.')
elif infracao <= via * 0.2:
    print('\nMulta de R$ 130,00 devido a ultrapassagem de até 20% do limite da via')
elif infracao <= via * 0.5:
    print('\nMulta de R$ 200,00 devida a ultrapassagem de 20% a 50% do limite da via')
else:
    print('\nMulta de R$ 500,00 e habilitação suspensa devido a ultrapassagem de mais de 50% do limite da via.')