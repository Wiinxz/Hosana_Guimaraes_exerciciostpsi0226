'''
Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
1, 1, 2, 3, 5, 8, 13, 21.


'''

soma1 =1
soma2 =1
bonachi = [soma1, soma2]

for i in range(58):

    resultado = soma1 + soma2
    soma1= soma2
    soma2 = resultado
    bonachi.append(resultado)
   
print(bonachi)

