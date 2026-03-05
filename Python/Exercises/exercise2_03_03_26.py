# EXERCISE 1 #

'''
 Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos.
Exemplo:
 Entrada: 3665 segundos
 Saída esperada: 1 hora, 1 minuto e 5 segundos. '''

input_seconds = int(input("Digite o número de segundos: "))

# o símbolo de // é uma divisao inteira, ou seja, o resultado é arredondado para baixo. 
hours = input_seconds // 3600 
remaining_seconds = input_seconds % 3600 # resto da divisão

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60 # resto da divisão

print(f"O resultado final é {hours} hora(s), {minutes} minuto(s) e {seconds} segundo(s).")