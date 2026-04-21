'''
Ordenação de Nomes com Base na Tabela ASCII
Recebeste uma lista com nomes completos de várias pessoas. A tua tarefa é ordená-los alfabeticamente, considerando o primeiro nome como critério principal e o apelido como critério de desempate, com base nos valores ASCII dos caracteres.
Lista de Nomes:
nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]
Regras:
1.	Ordena os nomes primeiro pelo primeiro nome comparando Caractere a Caractere.
2.	Se houver mais do que uma pessoa com o mesmo primeiro nome, usa o apelido como critério de desempate comparando Caractere a Caractere.
3.	Utiliza os valores ASCII implícitos na ordenação padrão de strings em Python (sem recorrer a bibliotecas).
Resultado Esperado:
Depois de ordenares, a lista deve ficar assim:
[
    "Ana Beatriz",
    "Ana Clara",
    "Ana Paula",
    "Beatriz Souza",
    "Carlos Silva",
    "Pedro Andrade",
    "Pedro Pereira"
]


'''

nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

def separar_nome_completo(nome_completo):
    
    partes = nome_completo.split(" ", 1)
    primeiro_nome = partes[0]
    apelido = partes[1] if len(partes) > 1 else ""
    return primeiro_nome, apelido


def ordenar_nomes(lista_nomes):

    print("Lista sem ordenar:")
    print(lista_nomes)

    # Cópia para não alterar a lista original
    ordenados = lista_nomes[:]

    tamanho = len(ordenados)

    # Bubble sort simples, comparando strings (ordem ASCII padrão do Python)
    for i in range(tamanho):
        for j in range(0, tamanho - 1 - i):
            nome_atual = ordenados[j]
            nome_seguinte = ordenados[j + 1]

            primeiro_atual, apelido_atual = separar_nome_completo(nome_atual)
            primeiro_seguinte, apelido_seguinte = separar_nome_completo(nome_seguinte)

            # 1º vou ordenar pelo primeiro nome
            precisa_trocar = primeiro_atual > primeiro_seguinte

            # 2ª vou ver se primeiro nome for igual e então desempatar pelo apelido
            if primeiro_atual == primeiro_seguinte:
                precisa_trocar = apelido_atual > apelido_seguinte

            if precisa_trocar:
                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]

    return ordenados


def main():
   # Vou usar a lista global novamente e preferi definir um main 
    global nomes

    nomes_ordenados = ordenar_nomes(nomes)
    print(nomes_ordenados)


if __name__ == "__main__":
    main()
