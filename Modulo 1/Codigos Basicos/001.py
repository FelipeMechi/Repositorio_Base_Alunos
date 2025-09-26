Olá, Mundo
tutorial variaveis
Oque são váriaveis
Váriaveis são espaços da memória do computador onde podemos guardar informações(como textos, números,resultados de cálculos,etc)para usar depois.

Váriaveis com texto (string)


nome = 'Raphael'
print(nome)
     
Raphael

print(nome)
     
Raphael
Váriavel com número inteiro (int)

idade = 16
print (idade)
     
16

#esse é um exemplo de um numero inteiro negativo
Temperatura = -3 #está variavel está armazenando um número negativo
print (Temperatura) #print () é uma função de saída
     
-3
Váriavel com número decimal (float)


altura = 1.62 #em python os números decimais são escritos com
#escritos com ".", exemplo 5.2
print (altura)
     
1.62

pi = 3.14
print(pi)
     
3.14
Váriavel com valor booleano (bool)


estudante = True
print(estudante)


     
True
Nomes de variáveis
pode :

Começar com letra

Conter número, mas não pode começar com números Não pode:

começar com número

usar espaço

usar acentuação ou caracteres especiais

usar palavras reservadas


#ERRADO
1idade = 16 # começar com número
meu nome = "Raphael" # espaço não é permitido
     
  File "/tmp/ipython-input-173815097.py", line 2
    1idade = 16 # começar com número
    ^
SyntaxError: invalid decimal literal
Oque é snake_case
snake_case é um estio de escrita usado para nome de variáveis,funções,e nomes em geral no código. Neste estilo,as palavras são todas em minúsculas e separadas por um undeline(_)

Por que usar snake_case?
deixa o código mais fácil de ler
É o padrão recomendado pela comunidade Python
Segue a PEF8,que é o guia de estilo oficial do python
OBS:PEF8 é um documento que recomenda boas práticas pra escrever código Python limpo legível.

Exemplos que não usam snake_case
nomeCompleto = "Maria" #estilo camelCase (mais comum em JavaScript) NomeCompleto = "Maria" # estilo PascalCase (usando para classes em Python) nomecompleto = "Maria" # estilo dificil de ler