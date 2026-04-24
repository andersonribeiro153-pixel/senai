h_pessoa = float(input("Digite sua altura (m): "))
s_pessoa = float(input("Digite o tamanho da sua sombra (m): "))
s_predio = float(input("Digite o tamanho da sombra do prédio (m): "))

h_predio = (h_pessoa * s_predio) / s_pessoa

print("Altura do prédio:", h_predio, "metros")