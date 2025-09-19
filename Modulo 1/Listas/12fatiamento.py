# Como fatiar uma lista?
# Podemos extrair "pedaços" da lista usando [início:fim:passo]:

letras = ["a", "b", "c", "d", "e"]

print(letras[1:4])   # ["b", "c", "d"] (índice 1 a 3)
print(letras[1:5])   # ["b", "c", "d", "e"] (índice 1 a 4)
print(letras[::2])   # ["a", "c", "e"] (pula de 2 em 2)
print(letras[::-1])  # ["e", "d", "c", "b", "a"] (inverte)