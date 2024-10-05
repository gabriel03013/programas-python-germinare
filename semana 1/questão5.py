# informações
tamanho_MB = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_Mbps = float(input("Digite a velocidade da conexão em Mbps: "))

# cálculos
tamanho_Megabits = tamanho_MB * 8
tempo_segundos = tamanho_Megabits / velocidade_Mbps
rapido = tempo_segundos <= 60

# resultado
print(f"Tempo estimado de download: {tempo_segundos:.2f} segundos")
print(f"Download rápido? {rapido}")