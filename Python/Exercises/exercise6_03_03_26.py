'''
Enunciado:

 Uma loja oferece descontos de acordo com o valor da compra:
10% para compras até 200,00€.
15% para compras entre 200,01€ e 500,00€.
20% para compras acima de 500,00€.

 Desenvolva um Programa que leia o nome do cliente e o valor da compra e mostre o valor do desconto e o valor total a pagar.
Exemplo:
 Entrada: Cliente: João, Compra: 350
 Saída esperada:
 Nome: João
 Compra: 350,00€
 Desconto: 52,50€
 Total a pagar: 297,50€

'''
name = input("Digite o nome do Cliente: ")
pay_value = float(input("Digite o valor da compra: "))
discont_value = 0

if pay_value <= 200.00 :
    discont_value = pay_value * 10 / 100
    print("Nome: ", name)
    print("Compra: ", pay_value)
    print("Desconto na compra é de 10%, com o total de: ",discont_value )
    print("Total á pagar: ", pay_value - discont_value )
elif pay_value >200.01 and pay_value <= 500.00 :
    discont_value = pay_value * 15 / 100
    print("Nome: ", name)
    print("Compra: ", pay_value)
    print("Desconto na compra é de 15%, com o total de: ",discont_value )
    print("Total á pagar: ", pay_value - discont_value )
else :
    discont_value = pay_value * 20 / 100
    print("Nome: ", name)
    print("Compra: ", pay_value)
    print("Desconto na compra é de 20%, com o total de: ",discont_value )
    print("Total á pagar: ", pay_value - discont_value )