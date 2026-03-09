'''
Operação matemática

Recebe uma operação (em texto) e dois números.
Operações válidas: "soma", "subtrai", "multiplica", "divide".

Exemplo:

Entrada →
Operação: "divide"
Número 1: 20
Número 2: 4
Saída → 5

'''
tipo = input("Digite a operação que desenha 'soma', 'subtracao','multiplicacao','divisão' :").lower()
num1 = int(input("Digite o 1ª número : "))
num2 = int(input("Digite o 2ª número : "))
result = 0

match(tipo):
  
  case _ if tipo [0:3] == "som":
    result = num1 + num2
    print(num1, " + " ,num2, " = " ,result)

  case _ if tipo[0:3] == "sub":
    result = num1 - num2
    print(num1, " - " ,num2, " = " ,result)
  
  case _ if tipo[0:3] == "mul":
    result = num1 * num2
    print(num1, " x " ,num2, " = " ,result)

  case _ if tipo[0:3] == "div":
    result = num1 / num2
    print(num1, " / " ,num2, " = " ,result)

  case _ :
    print("Opção inválida") 