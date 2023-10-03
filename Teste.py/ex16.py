horaInicio = int(input("Digite a hora de início do jogo: "))
horaFim = int(input("Digite a hora de fim do jogo: "))

if horaInicio == horaFim:
    duracao = 24 
elif horaInicio > horaFim:
    duracao = (24 - horaInicio) + horaFim
else:
    duracao = horaFim - horaInicio
print(f"A duração do jogo de xadrez foi de {duracao} horas.") 