'''
Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações
e no fim por meio de um acumulador diga quantas operações foram efetuadas. 

Exemplo 
introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.
'''

numero = int(input("Introduz um número: "))

totalOperacoes = 0

print("-----")
print("SOMAS ({numero} + i)")
print("-----")
for i in range(1, numero):
    print(f"{numero} + {i} = {numero + i}")
    totalOperacoes += 1

print("-----")
print("SUBTRAÇÕES({numero} + i)")
print("-----")
for i in range(1, numero):
    print(f"{numero} - {i} = {numero - i}")
    totalOperacoes += 1

print("-----")
print("MULTIPLICAÇÕES ({numero} + i)")
print("-----")
for i in range(1, numero):
    print(f"{numero} * {i} = {numero * i}")
    totalOperacoes += 1

print("-----")
print("DIVISÃO({numero} + i)")
print("-----")
for i in range(1, numero):
    print(f"{numero} / {i} = {numero / i:.2f}")
    totalOperacoes += 1

print("-----")
print(f"Total de operações efetuadas: {totalOperacoes}")
print("-----")