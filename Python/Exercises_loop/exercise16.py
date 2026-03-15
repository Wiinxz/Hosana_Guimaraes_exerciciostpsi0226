'''
Elabore um programa que constitua a média de 30 números pares que sejam introduzidos.

 Validando a entrada de números inteiros entre 1 e 50

'''
import random

pares = []

while len(pares) < 30:
    numero = random.randint(0, 50)
    
    if numero % 2 == 0:
        pares.append(numero)
        print(f"Gerado: {numero}", end=" |")
    

media = sum(pares) / len(pares)
print(f"\nMédia dos 3 pares: {media:.2f}")