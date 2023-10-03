quantidade_maca = int(input("Digite o número de maçãs compradas: "))
if quantidade_maca < 12:
    custo_unitario = 1.30
else:
    custo_unitario = 1.00
custo_total = custo_unitario * quantidade_maca
print(f"O custo total da compra é: R$ {custo_total:.2f}")