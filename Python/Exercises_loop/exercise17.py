'''
Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência.

'''


numeros = 0

for i in range (1,1001):

 if i % 5 == 0 and i % 3 != 0:
   print(f"o número {i} é multiplo de 5 e não multiplo de 3!")
  
 