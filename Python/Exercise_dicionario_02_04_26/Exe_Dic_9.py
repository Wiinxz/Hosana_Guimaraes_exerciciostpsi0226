'''
Exercício 9: Notas dos alunos

Cria um dicionário com o nome dos alunos e as suas respetivas listas de notas:
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

Calcula e imprime a média de cada aluno, com o seguinte formato:
João: 8.0
Maria: 9.0
Ana: 7.0


'''
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}


for aluno in notas:
    lista_notas = notas[aluno]

    
    soma = 0
    for nota in lista_notas:
        soma = soma + nota

    
    media = soma / len(lista_notas)

    print(aluno + ":", media)
