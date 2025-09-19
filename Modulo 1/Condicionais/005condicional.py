# Crie um código Python que verifique se a senha  digitada pelo usuário
# for "1234", exiba "Acesso perimitido".

# Etapas para resolução
# Criar uma variável e atribuir a ela uma senha
# Através de um input solicitar a senha ao usuário
# Através da condiconal checar se a senha é igual a senha armazenada
# liberar ou não o acesso ao usuário

senha_correta = "1234"

senha = input(" Digite sua senha: ")
if senha == senha_correta:
    print(" Acesso liberado. ")
else:
    print(" Acesso negado. Tente novamente")