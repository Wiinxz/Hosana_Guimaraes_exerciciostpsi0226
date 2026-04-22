'''
Exercício 4: Verificar se uma chave existe
Dado o dicionário:

utilizador = {'nome': 'Carlos', 'idade': 28}

Escreve um código que verifique se a chave email está presente no dicionário e imprima uma mensagem adequada, por exemplo: "Email não encontrado."


'''

utilizador = {'nome': 'Carlos', 'idade': 28}


if "email" in utilizador:
    print("Email encontrado:", utilizador["email"])
else:
    print("Email não encontrado.")