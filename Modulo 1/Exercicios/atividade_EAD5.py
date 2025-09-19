nome = input("Digite o nome do funcionário: ")
valor_vendas = float(input("Digite o valor total das vendas no mês (R$): "))
dias_trabalhados = int(input("Digite o número de dias úteis trabalhados no mês: "))

if valor_vendas > 10000 and dias_trabalhados >= 20:
    bonus = valor_vendas * 0.10
else:
    bonus = valor_vendas * 0.03

print("Resultado")
print(f"Funcionário: {nome}")
print(f"Vendas no mês: R$ {valor_vendas:,.2f}")
print(f"Dias úteis trabalhados: {dias_trabalhados}")
print(f"Bônus: R$ {bonus:,.2f}")
