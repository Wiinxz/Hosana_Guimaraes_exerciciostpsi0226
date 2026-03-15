'''
Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)

'''

numero = int(input("Introduz um número para ter a tabuada: "))
operacoes = 0

for i in range(1, numero +1):
    print(f"{numero} * {i} = {numero * i}")
    operacoes += 1