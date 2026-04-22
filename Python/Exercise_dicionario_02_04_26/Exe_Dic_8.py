'''
Exercício 8: Juntar dois dicionários

Dado os seguintes dicionários:
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

Cria um novo dicionário que contenha os pares chave-valor dos dois dicionários juntos.

'''
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = {}

# Copio os pares do primeiro dicionário
for chave in d1:
    d3[chave] = d1[chave]

# Copio os pares do segundo dicionário
for chave in d2:
    d3[chave] = d2[chave]

print(d3)
