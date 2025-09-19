# Crie um código python que peça o valor da conta. Se for maior que R$100,00 ,adicione uma
# gorjetade 10% e exiba o total a pagar.
# Caso contrário, adicione uma gorjeta de 5%

# Etapas para resolução
# 1) solicitar o valor da conta para o usuário
# 2) se a conta for maior que 100 adicione 10% de gorjeta e apresentar o total a pagar
# 3) se a conta for maior que 100 adicione 5% de gorjeta e apresentar o total a pagar 

valor_conta = float(input("Digite o valor da conta: R$ "))

if valor_conta >= 100:
    gorjeta = valor_conta * 0.10
else:
    gorjeta = valor_conta * 0.05

total_a_pagar = valor_conta + gorjeta
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
