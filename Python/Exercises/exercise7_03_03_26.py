'''
Enunciado:
 O sistema de avaliação de uma disciplina tem três provas com pesos diferentes. A primeira tem peso 2, a segunda tem peso 3, e a terceira tem peso 5. 
 Crie um programa para calcular a média final de um aluno e mostrar se ele está APROVADO (nota >= 6) ou REPROVADO (nota < 6).

 Exemplo:
 Entrada: Nota1 = 7, Nota2 = 6, Nota3 = 9
 Saída esperada:
 Média: 7.4
 Aprovado
'''
nota1= int(input("Digite a 1º nota: "))
nota2= int(input("Digite a 1º nota: "))
nota3= int(input("Digite a 1º nota: "))

media1 = nota1*2 / 10
media2 = nota2*3 / 10
media3 = nota3*5 / 10

media_final = media1 + media2 + media3

if media_final >=6 :
    print("O aluno está aprovado com média: ",media_final )
else:
    print("O aluno esta reprovado com média: ", media_final)
