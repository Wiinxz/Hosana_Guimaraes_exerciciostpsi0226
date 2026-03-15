'''
Exercício 9: Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100.
 (Use o ciclo do ... while)

'''

while True:
    numero = int(input("Adivinha o número (1 ou 100): "))
    if numero == 1 or numero == 100:
        break
    print(" Errado! Tenta novamente.")

print("Acertaste! O número é ", numero)


