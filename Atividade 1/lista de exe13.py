num = int(float(input("Digite um número até 3 dígitos: ")))

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

print("CENTENA =", centena)
print("DEZENA =", dezena)
print("UNIDADE =", unidade)