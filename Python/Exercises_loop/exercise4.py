'''
Exercício 4: Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

'''

import random

numero = random.randrange(3, 100)
divisor = 2
primo = True

while divisor < numero:
    if numero % divisor == 0:
        primo = False
        break
    divisor += 1

if primo:
    print("O número", numero, "é primo ")
else:
    print("O número", numero, "não é primo ")

