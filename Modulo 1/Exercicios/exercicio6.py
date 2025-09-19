senha_correta = "senha123"

senha = input(" Digite sua senha de wifi: ").strip().lower()
if senha == senha_correta:
    print("Conectado. ")
else:
    print("Senha incorreta. ")