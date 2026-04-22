'''
2. Ordenar uma lista de palavras por ordem alfabética inversa (Z → A), ignorando maiúsculas/minúsculas
Objetivo: Reordenar da última letra do alfabeto para a primeira, sem distinguir maiúsculas de minúsculas.

Exemplo:
["Python", "inteligência", "Aprender", "dados", "Rede"]
Resultado esperado:
["Rede", "Python", "inteligência", "dados", "Aprender"]

Como fazer:
•	Compara os caracteres em minúsculas ("A" e "a" passam a ser tratados como iguais).
•	Ordena da última letra para a primeira.
•	A lógica da comparação será invertida: em vez de colocar as menores primeiro, colocas as maiores.

'''

palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

for i in range(len(palavras)):
    for j in range(len(palavras) - 1 - i):

        # Converti para minúsculas só para comparar
        p1 = palavras[j].lower()
        p2 = palavras[j + 1].lower()

        trocar = False
        tamanho_menor = min(len(p1), len(p2))

        for t in range(tamanho_menor):
            if ord(p1[t]) < ord(p2[t]):  # invertido: para colocar o menor trás
                trocar = True
                break
            elif ord(p1[t]) > ord(p2[t]):
                break
        else:
            if len(p1) < len(p2):  # prefixo: o mais curto vai para trás
                trocar = True

        if trocar:
            palavras[j] = palavras[j + 1]
            palavras[j + 1] = palavras[j - 1 + 1]  # troco os originais

# Para escrever melhor a troca 
palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

for i in range(len(palavras)):
    for j in range(len(palavras) - 1 - i):
        if palavras[j].lower() < palavras[j + 1].lower():
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print("Resultado:", palavras)
