'''
3. Ordenar os caracteres de uma palavra por ordem alfabética

Objetivo: Pega numa palavra e reorganiza as suas letras da mais "baixa" para a mais "alta", segundo o valor ASCII.

Exemplo:
"algoritmo"
Resultado esperado:
"agilmootr"

Como fazer:
•	Divide a palavra em caracteres.
•	Ordena os caracteres com base no valor de ord().
•	Junta novamente numa string.
Este exercício é útil para aprender como a ordenação funciona mesmo a nível de caracteres, não só de palavras inteiras.

'''
palavra = "algoritmo"

# Converti a palavra numa lista com as letras
letras = list(palavra)  # ['a', 'l', 'g', 'o', 'r', 'i', 't', 'm', 'o']

# usei o Bubble Sort nas letras
for i in range(len(letras)):
    for j in range(len(letras) - 1 - i):
        if ord(letras[j]) > ord(letras[j + 1]):
            letras[j], letras[j + 1] = letras[j + 1], letras[j]

# Junto as letras de volta numa string
resultado = ""
for letra in letras:
    resultado = resultado + letra

print("Resultado:", resultado)
