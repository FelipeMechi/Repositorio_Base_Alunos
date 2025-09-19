# Crie um código em python que peça um número ao usuário e exiba "Número par" se ele for
# divisível por 2.

# Etapas de resolução:

# 1) solicitar um número ao usuário
# 2) verificar se o número é par ou ímpar
# 3) informar se o número é par ou ímpar

numero = float(input(" Digite um número: "))

if numero % 2 == 0: 
    print(f" O número {numero} é par.")
else:
    print(f" O número {numero} é ímpar.")