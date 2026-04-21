'''
1.	Ordenar uma lista de palavras por ordem alfabética (A → Z)
Objetivo: Reordenar as palavras, comparando carácter por carácter, como se estivesses a fazer o papel da função sorted().

Exemplo:
["banana", "uva", "abacaxi", "laranja"]
Resultado esperado:
["abacaxi", "banana", "laranja", "uva"]

Como fazer:
•	Compara as palavras duas a duas.
•	Usa o código ASCII de cada letra para decidir qual vem antes.
•	Se duas palavras começarem pela mesma letra, continua a comparação na letra seguinte.
•	Se uma palavra for prefixo da outra (como "casa" e "casamento"), a mais curta deve vir primeiro.

'''


palavras = ["banana", "uva", "abacaxi", "laranja"]

# Bubble Sort: percorre a lista várias vezes
for i in range(len(palavras)):
    for j in range(len(palavras) - 1 - i):
        palavra1 = palavras[j]
        palavra2 = palavras[j + 1]

        # Compara letra a letra
        trocar = False
        tamanho_menor = min(len(palavra1), len(palavra2))

        for k in range(tamanho_menor):
            if ord(palavra1[k]) > ord(palavra2[k]):
                trocar = True
                break
            elif ord(palavra1[k]) < ord(palavra2[k]):
                break
        else:
            # Se uma palavra é prefixo da outra, a mais curta vem primeiro
            if len(palavra1) > len(palavra2):
                trocar = True

        if trocar:
            palavras[j] = palavra2
            palavras[j + 1] = palavra1

print("Resultado:", palavras)
# meu resultado esperado é ['abacaxi', 'banana', 'laranja', 'uva']