''' Enunciado:
 Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. Analise se o cheque pode ser descontado.
 Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.

Exemplo:
 Entrada: Saldo = 500, Cheque = 300
 Saída esperada:
 Cheque descontado, saldo: 200 '''

bank_balance = float(input("Digite o seu saldo bancario atual: "))
check_value = float(input("Digite o valor do cheque á descontar "))

if bank_balance>check_value:
    update_value = bank_balance - check_value
    print("Seu cheque foi descontado, o saldo atual é: ", update_value )
else:
    print("O cheque não pode ser descontado, valor do cheque maior que o saldo bancario")
