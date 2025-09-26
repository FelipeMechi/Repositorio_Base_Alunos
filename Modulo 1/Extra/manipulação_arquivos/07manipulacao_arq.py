# Criar um arquivo nomes.txt

nomes = ['João\n','Maria\n','Ana\n'] # criarmos uma lista de nomes para ser
# inseridos no arquivo nomes.txt

with open('nomes.txt','w', encoding='utf-8') as arquivo: # estamos criando o arquivo
    arquivo.writelines(nomes) # estamos pedindo para escrever