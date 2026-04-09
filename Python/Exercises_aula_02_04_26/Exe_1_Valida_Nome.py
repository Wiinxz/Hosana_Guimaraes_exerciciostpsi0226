'''
Cria um programa que peça ao utilizador para introduzir o seu nome completo. O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.
Exemplo:
Pedro Pereira 

Se o nome for válido, o programa deve exibir:
 "Nome válido!"
Caso contrário, deve exibir:
 "Nome inválido: contém caracteres não permitidos."

No caso de o programa encontrar um caractere invalido deve parar a execução.

Exemplos Inválidos:
Miguel PriMo
Luis AnseLmo
Guilherme ramos

'''
def check_string(n):
    espera_maiuscula = True

    for letter in n:
        codigo = ord(letter)

        if espera_maiuscula:
            if 65 <= codigo <= 90:        # é maiúscula  = válido
                espera_maiuscula = False
            else:                          # devia ser maiúscula mas não é = inválido
                print("Nome inválido: contém caracteres não permitidos.")
                return False

        elif codigo == 32:                 # é espaço = ativa flag
            espera_maiuscula = True

        elif 97 <= codigo <= 122:          # é minúscula = válido
            pass

        else:                              # nada do anterior = inválido
            print("Nome inválido: contém caracteres não permitidos.")
            return False

    print(f"O Nome {n} é válido!")
    return True


nome = input("Introduz o teu nome completo: ")
check_string(nome)

