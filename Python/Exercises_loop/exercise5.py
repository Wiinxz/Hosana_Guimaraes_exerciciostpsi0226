'''
Exercício 5: Elabore um programa que escreve os primeiros 10.000 números inteiros no ecrã.

'''

import random

vezes = 0

while vezes < 10000:
 
 variosNumeros = random.randrange(1,100000)
 print(variosNumeros,end=" ")
 