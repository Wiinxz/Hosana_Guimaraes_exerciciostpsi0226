'''
Exercício 7: Inverter chaves e valores

Tens o seguinte dicionário:
d = {'a': 1, 'b': 2, 'c': 3}

Cria um novo dicionário que tenha os valores como chaves e as chaves como valores. Resultado esperado:
{1: 'a', 2: 'b', 3: 'c'}


'''

dicionario = {'a': 1, 'b': 2, 'c': 3}


dicionario_invertido = {}

for chave in dicionario:
    valor = dicionario[chave]
    dicionario_invertido[valor] = chave  # agora o valor é a chave e a chave é o valor

print(dicionario_invertido)
# Resultado: {1: 'a', 2: 'b', 3: 'c'}