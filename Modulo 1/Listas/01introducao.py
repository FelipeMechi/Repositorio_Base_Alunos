# LISTA

# SINTAXE
# Como Criar uma Lista?

# Usamos colchetes [ ] para definir uma lista, separando os elementos por vírgulas.
# nome_da_lista = [elemento_0, elemento_1, elemento2]

diversos =[1,'banana', 'mouse', 23.5,'aeiou', True, [1,2,3,4,5]]
        # 0,    1,      2,      3,      4,      5,      6
# Isso mostra que listas são flexíveis e podem misturar tipos de dados.

print(diversos) # lista total
print(diversos[3]) # a lista começa com índice zero, então, o 3° elemento é "23.5"
print(diversos[-1]) # pegar o último elemento, quando eu não sei o tamanho da lista
print(diversos[6]) # pegar um elemento específico
print(diversos[-1][2]) # pegar um elemento da lista dentro de outra lista
