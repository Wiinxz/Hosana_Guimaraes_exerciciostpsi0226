print ("Hello World TPSI0226")

val1 = 2
val2 = 3
val3 = 4

    # primeira hipotese aonde o maior é o val1 
if val1> val2 and val2>val3:
    print ("O maior valor é o valor1 ", val1, "O menor valor é o valor3 ", val3)
elif val1> val3 and val3>val2:
    print ("O maior valor é o valor1 ", val1, "O menor valor é o valor2 ", val2)

# segunda hipotese aonde o maior é o val2
elif val2> val1 and val1>val3:
    print ("O maior valor é o valor2 ", val2, "O menor valor é o valor3 ", val3)
elif val2> val3 and val3>val1:
    print ("O maior valor é o valor2 ", val2, "O menor valor é o valor1 ", val1)    

# terceira hipotese aonde o maior é o val3
elif val3> val1 and val1>val2:
    print ("O maior valor é o valor3 ", val3, "O menor valor é o valor2 ", val2)
elif val3> val2 and val2>val1:
    print ("O maior valor é o valor3 ", val3, "O menor valor é o valor1 ", val1)

