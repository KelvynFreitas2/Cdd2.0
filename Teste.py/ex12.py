
totalEleitores = int(input("Digite o número total de eleitores: "))
votosBrancos = int(input("Digite o número de votos brancos: "))
votosNulos = int(input("Digite o número de votos nulos: "))
votosValidos = int(input("Digite o número de votos válidos: "))

percentual_brancos = (votosBrancos / totalEleitores) * 100
percentual_nulos = (votosNulos / totalEleitores) * 100
percentual_validos = (votosValidos / totalEleitores) * 100

# Exibe os resultados
print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")