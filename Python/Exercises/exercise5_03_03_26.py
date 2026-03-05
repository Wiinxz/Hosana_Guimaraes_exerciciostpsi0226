'''
Enunciado:
 Ler 3 valores inteiros e apresentar os valores dispostos em ordem crescente e decrescente.

Exemplo:
 Entrada: num1 = 4, num2 = 9, num3 = 2
 Saída esperada:
 Crescente: 2, 4, 9
 Decrescente: 9, 4, 2
'''
num1 = int(input("Digite o 1ª número: "))
num2 = int(input("Digite o 2ª número: "))
num3 = int(input("Digite o 3ª número: "))


if num1>num2 and num1>num3 and num2>num3 :  #hipostese onde o 1ª é o maior
  print("Em ordem crescente",num3, num2, num1)
  print("Em ordem decrescente",num1, num2, num3)
elif num2<num3 and num1>num3:  # se o num 2º for o menor que o 3ª
   print("Em ordem crescente",num2, num3, num1)
   print("Em ordem decrescente",num1, num3, num2)
  

elif num2>num1 and num2>num3 and num1>num3 :  #hipotese aonde o 2º é o maior
  print("Em ordem crescente",num3, num1, num2)
  print("Em ordem decrescente",num2, num1, num3)
elif num1 < num3 and num1 > num2:  # agora verifico que o 1ª está entre 2ª e 3ª
   print("Em ordem crescente",num2, num1, num3)
   print("Em ordem decrescente",num3, num1, num2)

elif num3>num1 and num3>num2 and num1>num2 :  #hipotese aonde o 3º é o maior
  print("Em ordem crescente",num2, num1, num3)
  print("Em ordem decrescente",num3, num1, num2)
elif num1<num2: # se o num 1ª for menor que o 2ª
   print("Em ordem crescente",num1, num2, num3)
   print("Em ordem decrescente",num3, num2, num1)


