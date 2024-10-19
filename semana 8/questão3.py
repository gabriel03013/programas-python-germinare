germ_tech = int(input('Digite a quantidade de alunos da Germinare TECH: '))
germ_business = int(input('Digite a quantidade de alunos da Germinare BUSINESS: '))
anos = 0

while germ_tech < germ_business:
    germ_tech += germ_tech * 0.5
    germ_business += germ_business * 0.1
    anos += 1

print(f'Vai demorar {anos} anos para a quantidade de alunos da Germinare TECH ultrapassar a quantidade de alunos da Germinare BUSINESS ')