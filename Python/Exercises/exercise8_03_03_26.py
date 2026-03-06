'''
Enunciado:
Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. 
Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 

'''
resposta = int(input("Digite uma nota: "))
nota1 = resposta
resposta = int(input("Digite uma nota: "))
nota2 = resposta
resposta = int(input("Digite uma nota: "))
nota3 = resposta
resposta = int(input("Digite uma nota: "))
nota4 = resposta
resposta = int(input("Digite uma nota: "))
nota5 = resposta
resposta = int(input("Digite uma nota: "))
nota6 = resposta
resposta = int(input("Digite uma nota: "))
nota7 = resposta
resposta = int(input("Digite uma nota: "))
nota8 = resposta
resposta = int(input("Digite uma nota: "))
nota9 = resposta
resposta = int(input("Digite uma nota: "))
nota10 = resposta

media = (nota1 + nota2 + nota3 + nota4 * 10) / 20

print("Média final das notas foi : ", media)
acima_da_media = 0
abaixo_da_media = 0

if nota1 >= media :
  acima_da_media +=1

if nota2 >= media :
  acima_da_media +=1

if nota3 >= media :
  acima_da_media +=1

if nota4 >= media :
  acima_da_media +=1

if nota5 >= media :
  acima_da_media +1

if nota6 >= media :
  acima_da_media +1

if nota7 >= media :
  acima_da_media +1

if nota8 >= media :
  acima_da_media +1

if nota9 >= media :
  acima_da_media +1

if nota10 >= media :
  acima_da_media +1

print ("Um total de", acima_da_media,"alunos igual ou acima da média")