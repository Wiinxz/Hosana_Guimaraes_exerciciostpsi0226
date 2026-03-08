'''
Tipo de pedido

Recebe um dicionário com as chaves "tipo" e "valor".
Exibe:
•	“Compra de X€” se tipo for “compra”
•	“Venda de X€” se tipo for “venda”
•	“Pedido desconhecido” caso contrário

Exemplo:
Entrada → {"tipo": "venda", "valor": 250}
Saída → Venda de 250€

'''
# ia criar o exercicio para o utilizador inserir o input, mas o enunciado diz que recebe apenas o dicionário já feito e o que importa é a frase de output
#tipo = input(" Digite se é 'venda' ou 'compra'").islower()
#valor = int(input("Digite o valor"))

pedido = {"tipo":"compra", "valor": 250}

if pedido["tipo"] == "venda":
 print("Venda de", pedido.get("valor"))

elif pedido["tipo"] == "compra":
  print("Compra de",pedido.get("valor"))

else:
  print("Pedido desconhecido!")


