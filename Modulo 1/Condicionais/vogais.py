# Peça ao usuário para digitar uma letra
# Se for vogal, informe qual vogal
# Se for consoante, verifique se é maiúscula ou minúscula

# Solicitação de entrada de dados de tipo string (texto)
letra = input("Digite uma letra: ")

if letra.lower() in "aeiou": # .lower() transforma para minúscula
    print(f'Vogal {letra}')
else:
    if letra.isupper(): # isupper identifica se a letra está em maiúscula
        print(f"Consoante maiúscula: {letra} ")
    else:
        print(f"Consoante minúscula: {letra} ")
