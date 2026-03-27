'''
 Teste Final: Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 (se é número Primo, 
 Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores
 com instrução para parar ou continuar. No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) 
 com a função extra tabuada. Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao 
 máximo introduzido) deve parar de 20 em 20 valores.

 '''


# DEMOREI A ENTREGAR PORQUE QUERIA TERMINAR O MÓDULO 3 DO NETCAD E USEI def E TAMBÉM RETURN QUE APRENDI UM POUCO LÁ NESSE EXERCÍCIO
program_on = True

def menu():

    print("\nChoose an option:")
    print("[1] - Look at prime numbers, number of divisors and perfect numbers up to that number.")
    print("*CHOOSE [1] only accepts values from 1 to 30.000*\n")

    print("[2] - Use calculator and multiplication table")
    print("*CHOOSE [2] only accepts values from 1 to 1.000*\n")

    option = int(input("Option: "))
    return option


def e_primo(n):
    if n < 2:
        return False

    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    return divisores == 2


def contar_divisores(n):
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores


def e_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i

    return soma == n and n != 0


def analisar_numeros(limite):

    contador = 0

    for n in range(limite, 0, -1):
        primo = e_primo(n)
        qtd_div = contar_divisores(n)
        perfeito = e_perfeito(n)

        print(f"\nNumber: {n}")
        print(f"Prime? {primo}")
        print(f"How many divisors? {qtd_div}")
        print(f"Perfect number? {perfeito}")

        contador += 1

        if contador % 10 == 0 and n != 1:
            usr_resp = input("\nDo you want to continue? (s/n): ").lower()
            if usr_resp != "s":
                break


def tabuada(n):
    contador = 0

    for i in range(1, n + 1):
        print(f"{n} * {i} = {n * i}")
        contador += 1

        if contador % 20 == 0 and i != n:
            usr_resp = input("\nDeseja continuar? (s/n): ").lower()
            if usr_resp != "s":
                break


def calculation(opc, n):
    match opc:
        case 1:

            valor2 = int(input("Enter the second value: "))
            if valor2 < 1 or valor2 > 1000:
                print("The limit is from 1 to 1000!")
            else:
                print(f"Result: {n} + {valor2} = {n + valor2}")

        case 2:

            valor2 = int(input("Enter the second value: "))
            if valor2 < 1 or valor2 > 1000:
                print("The limit is from 1 to 1000!")
            else:
                print(f"Result: {n} - {valor2} = {n - valor2}")

        case 3:

            valor2 = int(input("Enter the second value: "))
            if valor2 < 1 or valor2 > 1000:
                print("The limit is from 1 to 1000!")
            else:
                print(f"Result: {n} * {valor2} = {n * valor2}")

        case 4:

            valor2 = int(input("Enter the second value: "))
            if valor2 < 1 or valor2 > 1000:
                print("The limit is from 1 to 1000!")
            else:
                print(f"Result: {n} / {valor2} = {n / valor2}")

        case 5:
            tabuada(n)

        case _:
            print("That option isn't available, please try again!")


while program_on:

    option = menu()

    if option != 1 and option != 2:
        print("Choose option 1 or 2!!!!!")
        continue

    number_value = int(input("Enter a value to calculate:\n"))

    match option:

        case 1:

            if number_value < 1 or number_value > 30000:
                print("The limit is from 1 to 30.000! Start again.\n")
                continue

            analisar_numeros(number_value)

        case 2:

            if number_value < 1 or number_value > 1000:
                print("The limit is from 1 to 1.000! Start again.\n")
                continue

            print("\nWhich calculation do you want to perform?")
            print("[1] - SUM +")
            print("[2] - SUBTRACTION -")
            print("[3] - MULTIPLICATION *")
            print("[4] - DIVISION /")
            print("[5] - MULTIPLICATION TABLE")

            opc_calculation = int(input("Option: "))
            calculation(opc_calculation, number_value)

    sair = input("\nDo you want to go back to the menu? (s/n): ").lower()

    if sair != "s":
        program_on = False