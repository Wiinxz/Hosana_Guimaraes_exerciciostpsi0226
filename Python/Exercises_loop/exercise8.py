'''
Exercício 8: Faça um algoritmo que gere a seguinte série: 10, 20, 30, 40, ..... 980, 990, 1000.e outro a fazer 15, 25, 35, 985, 995.(dois ciclos)

'''
vezes = 0
vezes2 = 5

while vezes < 1000:  #10,20,30,40....
     
     salto = 10
     vezes = vezes + 10
     print(vezes,end = " ")
     vezes +10

print("\n\n")

while vezes2 < 995: # 15,25,35,45...

     salto = 10
     vezes2 = vezes2 + 10
     print(vezes2,end = " ")
     vezes2 +10   

