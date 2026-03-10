'''

Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

'''

import random

numero =  random.randint(1,61)

for numero in range(1,61):

    if numero % 2 == 0:
     print("\nnumeros pares",numero)


for numero in range (1,61):

    if numero % 2 == 1:
      
       print("\nnúmeros impares",numero)
