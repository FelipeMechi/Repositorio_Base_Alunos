valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra >= 150:
    valor_final = valor_compra - 20
    print(f"Desconto de R$20,00 aplicado. Valor final: R$ {valor_final:.2f}")
else:
    valor_final = valor_compra
    print(f"Nenhum desconto aplicado. Valor final: R$ {valor_final:.2f}")
