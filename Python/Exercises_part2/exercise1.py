'''
1. Tipo de dia
Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.

Exemplo:
Entrada → domingo
Saída → Fim de semana

'''
dias = [ "segunda", "terça", "terca", "quarta", "quinta", "sexta", "sabado", "sábado", "domingo" ]
dia_usuario = input("Digite um dia da semana: ")

if dia_usuario not in dias:
    print("Dia inválido")
elif dia_usuario in [ "sabado", "sábado", "domingo" ]:
    print("Fim de semana 😎")
else :
    print("Dia de semana 😔")
