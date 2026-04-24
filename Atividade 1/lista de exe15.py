total = float(input("Digite o valor total da conta: "))

parte = total / 3

carlos = int(parte)
andre = int(parte)

felipe = total - (carlos + andre)

print("Carlos:", carlos)
print("André:", andre)
print("Felipe:", round(felipe, 2))