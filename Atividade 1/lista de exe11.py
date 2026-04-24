total_dias = float(input("Digite o total de dias: "))

anos = int(total_dias // 360)
resto = total_dias % 360

meses = int(resto // 30)
dias = resto % 30

print("Anos:", anos)
print("Meses:", meses)
print("Dias:", dias)