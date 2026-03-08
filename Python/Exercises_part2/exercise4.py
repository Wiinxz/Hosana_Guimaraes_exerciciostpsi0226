'''
Tipo de dado

Analisa um valor e retorna o seu tipo:
•	Número inteiro
•	Número decimal
•	String numérica
•	String textual
•	Lista
•	Tipo desconhecido 

Exemplo:
Entrada → [10, 20, 30]
Saída → Lista

'''

# pensei em usar um eval, porém estive a ler que input() apenas lê texto e eval(input()) lê o texto e depois tenta avaliá-lo como expressão Python.
#queria considerar que se o utlizador escrevesse algo como "as45s4d5a4da4d5a4" ou "5+5+5+" fosse caracterzado como string

utilizador = input("Insira algo para descobrir o tipo de dado: ")

match utilizador:
  
   case str() as utilizador:
    
    if utilizador[0] == "[":
     print("É lista")

    elif "." in utilizador:
      print("Número decimal")

    elif utilizador[0] == "-":
      print("Número negativo")
    
    elif utilizador.isdigit():
      print("Número inteiro")    
    else:
      print("String")
    
   case _ :
    print("Tipo desconhecido 🤔")
    
