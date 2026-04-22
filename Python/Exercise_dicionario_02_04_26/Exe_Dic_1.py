'''
Exercício 1: Criar um dicionário simples

Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
1-	Inserir
2-	Listar

O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
Exemplo:

nome: Maria
idade: 20
curso: Engenharia

'''
alunos = {}
 

alunos["nome"] = input("Introduz o nome do aluno: ")
alunos["idade"] = int(input("Introduz a idade do aluno: "))
alunos["curso"] = input("Introduz o curso do aluno: ")
 

print("nome:", alunos["nome"])
print("idade:", alunos["idade"])
print("curso:", alunos["curso"])