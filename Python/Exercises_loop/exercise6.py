'''
Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos.

'''

divisor = 2
primo = True
vezes = 0
numero = 2

while vezes < 10:
    primo = True
    divisor = 2

    while divisor < numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print(numero,end=" ")
        vezes += 1

    numero += 1



        


     


  
    


