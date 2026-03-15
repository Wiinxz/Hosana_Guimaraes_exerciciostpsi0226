'''
Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. 
Dispor de 20 em 20 com a condição de continuação ou saída do programa.
'''

for i in range(0, 256, 20):
    for j in range(i, min(i + 20, 256)):
        print(f"Código: {j:3} -  Caractere: {chr(j)}")

    if i + 20 >= 256:
        print("Fim da tabela!")
        break

    resposta = input("\nDeseja continuar? (s/n): ").lower()
    if resposta != "s":
        break


#não sei como imprimir todos exatamente como esta na tabela ASCII, 
# usei o chr para me dizer qual o char de acordo com o que está em cada posição mas não imprime todos