'''
Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média.

'''
import random
notas = []
vezes = 0

while vezes < 10:
    nota = random.randrange(1,21)
    print("as notas foram", nota)
    notas.append(nota)
    vezes +=1
    
media = sum(notas) / len(notas)
print("A média final foi : ", media)    

