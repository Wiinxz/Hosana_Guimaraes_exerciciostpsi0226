'''
5. Agrupar palavras pela letra inicial e ordenar cada grupo por ordem alfabética (A → Z)
Objetivo: Reorganizar as palavras em grupos que comecem com a mesma letra, e depois ordenar cada grupo manualmente.

Exemplo:
["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

Resultado esperado:
{
  'b': ['banana', 'bola'],
  'a': ['abacaxi', 'arroz'],
  'u': ['urso', 'uva']
}

Como fazer:
•	Cria um dicionário onde cada chave é uma letra inicial.
•	Coloca cada palavra no grupo correspondente.
•	Ordena cada grupo individualmente usando comparação com ord().
Este é o exercício mais completo: vais precisar de organizar, comparar e ordenar em dois níveis.


'''

palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

# Criei o dicionário de grupos
grupos = {}

for palavra in palavras:
    letra_inicial = palavra[0]  # primeira letra da palavra

    if letra_inicial not in grupos:
        grupos[letra_inicial] = []  # crio uma lista vazia para essa letra

    grupos[letra_inicial].append(palavra)  # adiciono a palavra ao grupo

# ordeno cada grupo manualmente com o Bubble Sort
for letra in grupos:
    lista = grupos[letra]

    for i in range(len(lista)):

        for j in range(len(lista) - 1 - i):
            p1 = lista[j]
            p2 = lista[j + 1]
            tamanho_menor = min(len(p1), len(p2))
            trocar = False

            for k in range(tamanho_menor):
                if ord(p1[k]) > ord(p2[k]):
                    trocar = True
                    break
                elif ord(p1[k]) < ord(p2[k]):
                    break
            else:
                if len(p1) > len(p2):
                    trocar = True

            if trocar:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# mostro o resultado
for letra in grupos:
    print(letra, ":",grupos[letra])

