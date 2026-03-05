'''
'''
val1 = int(input("Digite o 1ª valor: "))

val2 = int(input("Digite o 2ª valor: "))

val3 = int(input("Digite o 3ª valor: "))

    # primeira hipotese aonde o maior é o val1 
if val1> val2 and val2>val3:
    print ("O maior valor é o 1ºvalor: ", val1, ", O menor valor é o 3ºvalor: ", val3)
elif val1> val3 and val3>val2:
    print ("O maior valor é o 1ºvalor: ", val1, ", O menor valor é o 2ºvalor: ", val2)

# segunda hipotese aonde o maior é o val2
elif val2> val1 and val1>val3:
    print ("O maior valor é o 2ºvalor: ", val2, ", O menor valor é o 3ºvalor: ", val3)
elif val2> val3 and val3>val1:
    print ("O maior valor é o 2ºvalor: ", val2, ", O menor valor é o 1ºvalor: ", val1)    

# terceira hipotese aonde o maior é o val3
elif val3> val1 and val1>val2:
    print ("O maior valor é o 3ºvalor: ", val3, ", O menor valor é o 2ºvalor: ", val2)
elif val3> val2 and val2>val1:
    print ("O maior valor é o 3ºvalor: ", val3, ", O menor valor é o 1ºvalor: ", val1)

# se os valores forem iguais o programa quebra haha, o enunciado não disse nada sobre validar numeros iguais.
# No futuro vou ser mais detalhista :) 
