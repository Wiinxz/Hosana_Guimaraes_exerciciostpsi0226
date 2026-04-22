'''
Exercício 3: Cria um dicionário vazio chamado produto. Em seguida:

1.	Adiciona os seguintes pares chave-valor:
o	nome: "Telemóvel"
o	preço: 1500
o	stock: 30

2.	Remove a chave stock do dicionário.

3.	Imprime o dicionário final.


'''


produto = {}

produto["nome"] = "Telemóvel"
produto["preço"] = 1500
produto["stock"] = 30

del produto["stock"]

print(produto)
