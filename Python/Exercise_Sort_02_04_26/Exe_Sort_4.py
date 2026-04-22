'''
4. Ordenar uma lista de palavras pela quantidade de letras minúsculas
 Objetivo: Contar quantas letras minúsculas há em cada palavra e ordená-las do menor para o maior número.

Exemplo:
["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
Resultado esperado:
["CÓDIGO", "intELIGENTE", "PYthon", "dados", "banana"]

Como fazer:
•	Conta, para cada palavra, quantos caracteres estão entre 'a' e 'z'.
•	Usa esse número como "peso" para ordenar.
•	Palavras com mais minúsculas vão para o fim da lista.

'''

palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

# Conto as letras minúsculas da palavra
def contar_minusculas(palavra):
    contador = 0
    for letra in palavra:
        if 'a' <= letra <= 'z':  # verifica se é minúscula
            contador = contador + 1
    return contador

# Uso Bubble Sort com o número de minúsculas como peso
for i in range(len(palavras)):
    for j in range(len(palavras) - 1 - i):
        peso1 = contar_minusculas(palavras[j])
        peso2 = contar_minusculas(palavras[j + 1])
        if peso1 > peso2:
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print("Resultado:", palavras)
