'''
Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. 

Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
6=3+2+1 .

'''
perfeito = []

numero = int(input("Digite um número para saber se ele é perfeito: "))

for i in range (1,numero):

 if numero % i == 0:
   perfeito.append(i)

if sum(perfeito) == numero:
    print("Este numero é perfeito!")
    print(f"Divisores : {perfeito} == {numero}")
    
else:
    print(f"O número {numero} não é perfeito\n8")
    print("CURIOSIDADE: entre 1 e 1000 apenas 2 números são perfeitos, adivinhe...")
  
   


    
  
