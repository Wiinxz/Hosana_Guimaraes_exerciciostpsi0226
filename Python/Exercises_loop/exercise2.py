'''
Exercício 2: Ler 10 números, e determinar se o número par e número impar.

'''

import random
vezes = 0
numeros = 0

while vezes < 10:
    
    numeros = random.randrange(1,100)

    if numeros % 2 ==0:
        print(numeros,"é par")
    
    else:
        print(numeros,"é ímpar")
    vezes +=1


