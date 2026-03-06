'''
Enunciado:
 Leia 10 números e determine quantos são pares e quantos são ímpares.

Exemplo:
 Entrada: 2, 3, 5, 6, 8, 9, 10, 12, 14, 15
 Saída esperada:
 Pares: 6
 Ímpares: 4

'''
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
num6 = int(input("Digite um número: "))
num7 = int(input("Digite um número: "))
num8 = int(input("Digite um número: "))
num9 = int(input("Digite um número: "))
num10 = int(input("Digite um número: "))

par = 0
impar = 0

if num1 % 2 == 0:
  par+=1
else :
  impar+=1

if num2 % 2 == 0:
  par+=1
else :
  impar+=1

if num3 % 2 == 0:
  par+=1
else :
  impar+=1

if num4 % 2 == 0:
  par+=1
else :
  impar+=1

if num5 % 2 == 0:
  par+=1
else :
  impar+=1

if num6 % 2 == 0:
  par+=1
else :
  impar+=1

if num7 % 2 == 0:
  par+=1
else :
  impar+=1

if num8 % 2 == 0:
  par+=1
else :
  impar+=1

if num9 % 2 == 0:
  par+=1
else :
  impar+=1

if num10 % 2 == 0:
  par+=1
else :
  impar+=1

  print("Existem ", par ," números pares e ", impar,"números ímpares")