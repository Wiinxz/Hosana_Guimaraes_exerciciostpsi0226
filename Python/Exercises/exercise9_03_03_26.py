'''
Enunciado:
Leia um número inteiro de 1 a 12 e mostre o nome do mês correspondente. Caso o número não seja válido, mostre uma mensagem de erro.

Exemplo:
 Entrada: 5
 Saída esperada: Maio

'''
number = input("Digite um número de 1 á 12 para ver o mês correspondente: ")
match number:
        
    case "1":
            print("Janeiro")
    case "2":
            print("Fevereiro")
    case "3":
            print("Março")
    case "4":
            print("Abril")
    case "5":
            print("Maio")
    case "6":
            print("Junho")
    case "7":
            print("Julho")
    case "8":
            print("Agosto")
    case "9":
            print("Setembro")
    case "10":
            print("Outubro")
    case "11":
            print("Novembro")
    case "12":
            print("Dezembro")
    case _:
            print("Opcao errada :( ")
   