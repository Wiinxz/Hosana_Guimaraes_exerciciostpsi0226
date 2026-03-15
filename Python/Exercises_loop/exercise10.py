'''
Elabore um programa que lê um número e escreve quantos divisores ele possui

'''

numero = int(input("Introduz um número: "))

contador = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

print("O número",numero,"tem",contador,"divisor(es).")
