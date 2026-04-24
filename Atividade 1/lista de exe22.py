m1 = float(input("Quantidade de moedas de 1 centavo: "))
m5 = float(input("Quantidade de moedas de 5 centavos: "))
m10 = float(input("Quantidade de moedas de 10 centavos: "))
m25 = float(input("Quantidade de moedas de 25 centavos: "))
m50 = float(input("Quantidade de moedas de 50 centavos: "))
m1real = float(input("Quantidade de moedas de 1 real: "))

total = (m1 * 0.01) + (m5 * 0.05) + (m10 * 0.10) + \
        (m25 * 0.25) + (m50 * 0.50) + (m1real * 1)

print("Total economizado: R$", total)