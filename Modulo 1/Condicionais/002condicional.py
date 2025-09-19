# Crie um código que receba 3 notas, calcule a média e informe se o
# aluno etsá, aprovado, em recuperação ou reprovado:

# OBS: Aprovado media >= 7
# Recuperação média > 4
# Reprovado média < 4

# Etapas
# 1) Solicitar as notas ao usuário
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
# 2) Calcular a média
media = (n1 + n2 + n3)/3
# 3) Checar a condição do aluno
# 4) Informar o resultado
if media >= 7:
    print(f"O aluno tem média {media:.2f} e está aprovado.")
elif 5 <= media < 7: # o mesmo que => elif media >= 5 and media < 7
    print(f"O aluno teve média {media:.2f} e está em recuperação.")
else:
    print(f"O aluno teve média {media:.2f} e está reprovado.")
