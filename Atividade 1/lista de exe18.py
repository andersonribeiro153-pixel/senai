h_normais = float(input("Horas normais: "))
h_extras = float(input("Horas extras: "))

bruto = (h_normais * 10) + (h_extras * 15)
liquido = bruto * 0.90

print("Salário bruto:", bruto)
print("Salário líquido:", liquido)