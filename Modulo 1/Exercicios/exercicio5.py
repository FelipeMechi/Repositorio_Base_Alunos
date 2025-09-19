valor_conta = float(input("Digite o valor da conta: R$ "))

if valor_conta >= 100:
    gorjeta = valor_conta * 0.10
else:
    gorjeta = valor_conta * 0.05

total_a_pagar = valor_conta + gorjeta
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
