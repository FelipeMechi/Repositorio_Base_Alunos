Função print ()
a funão print () é uma das funções mais importantes e usadas na linguagem Python, Sua função é basicamente, exibir mensagens na tela ou envia-las para outro dispositivo,como imprimir dentro de um arquivo de texto.

No Python 3, print() é uma função interna, de modo que não é necessário importar nenhuma bicicleta para poder ultiliza-lá. Basta chaá-la e passar os argumentos necessários.


print( "Meu primeiro print") # todo o texto deve estar entre aspas simples ou duplas
     
Meu primeiro print

print("D'água") # é quando uma palavra contém aspas às aspas iniciais devem ser diferentes
     
D'água

print(20 + 15) # o Python realiza a operação que está dentro do parenteses
     
35

print ("20 + 15") # é a operação entre aspas será apenas impressa não executada
#pois o python entende isso com o texto
     
20 + 15

print ("20 + 15 = ", 20 + 15)
     
20 + 15 =  35

n1 = "1"
n2 = "3"
print(n1 + n2) #concatenação quando Python junta 2 strings
     
13

n1 = "b"
n2 = "a"
print(n1 + n2)
     
ba

nome = "Raphael"
sobrenome = "Monteiro"
nome_completo = nome + " " + sobrenome
print(nome_completo)

     
Felipe Mechi