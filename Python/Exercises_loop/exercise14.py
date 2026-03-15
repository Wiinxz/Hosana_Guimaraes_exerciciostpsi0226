'''
Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).

'''

numero = int(input("Introduz um número para ter a tabuada: "))
operacoes = 0

for i in range(1, 101):
    print(f"{numero} * {i} = {numero * i}")
    operacoes += 1