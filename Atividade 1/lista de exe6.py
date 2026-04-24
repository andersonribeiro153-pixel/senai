while True:
    
    peso_prato = float(input("Digite o peso do prato pelo cliente (em Quilos)"))
    if peso_prato >=0:
        break
    print("valor Invalido")

    valor_a_pagar = peso_prato * 12.0
    print ("o valor a pagar é de R$:",valor_a_pagar)