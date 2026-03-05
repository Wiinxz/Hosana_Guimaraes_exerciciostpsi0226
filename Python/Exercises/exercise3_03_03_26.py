'''
Enunciado:
 Crie 2 variáveis (num1 e num2) e leia o valor para cada uma delas. Mostre os valores de forma crescente e decrescente.

Exemplo:
 Entrada: num1 = 7, num2 = 2
 Saída esperada:
 Crescente: 2, 7
 Decrescente: 7, 2

'''

num1 = int(input("Digite o 1ª número: "))
num2 = int(input("Digite o 2ª número: "))

if num1>num2:
 print("Em ordem crescente",num2 , num1)
 print("Em ordem decrescente",num1 , num2)

else:
  print("Em ordem crescente",num1 , num2)
  print("Em ordem decrescente",num2 , num1)