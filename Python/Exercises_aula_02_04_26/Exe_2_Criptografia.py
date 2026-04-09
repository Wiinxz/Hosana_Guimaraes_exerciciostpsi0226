'''
Cria um programa que criptografe e descriptografe mensagens utilizando a tabela ASCII e uma chave String. A chave será uma palavra ou frase fornecida pelo utilizador, e a criptografia será feita com base na soma dos valores ASCII dos caracteres dessa chave.
Funcionamento da Criptografia
1.	O utilizador introduz:
o	Uma mensagem (ex: "Olá Mundo")
o	Uma chave em formato de string (ex: "chave")
2.	O programa:
o	Calcula a chave numérica, somando os valores ASCII de cada letra da chave:
	"chave" → 'c'=99, 'h'=104, 'a'=97, 'v'=118, 'e'=101
Soma: 99 + 104 + 97 + 118 + 101 = **519**
o	Usa essa soma (519) como valor para criptografar cada caractere da mensagem:
	'O' → ord('O') = 79 → 79 + 519 = 598
	'l' → ord('l') = 108 → 108 + 519 = 627
	etc.
3.	Para descriptografar, o programa deve subtrair o mesmo valor (519 neste caso) de cada número para recuperar os caracteres originais.
Requisitos:
1.	O programa deve conter três funções:
o	criptografar(mensagem: str, chave: str) -> List[int]
o	descriptografar(codigos: List[int], chave: str) -> str
o	listar_codigos
2.	Utilizar apenas funções nativas (ord() e chr()).
3.	Manter os espaços, acentos e distinguir entre maiúsculas e minúsculas.
4.	Impede que a chave seja vazia.
5.	Aplica rotação aos caracteres da mensagem encriptada (entre ASCII 32 e 126), para mantê-los dentro deste intervalo.

'''
# Coloquei alguns Limites dos caracteres ASCII "imprimíveis", não validei acentos
ascii_inicio = 32
ascii_fim = 126
intervalo_ascii = ascii_fim - ascii_inicio + 1


lista_codigos = []

def calcular_chave_numerica(chave):

    # Valido a chave
    if chave == "":
        raise ValueError("A chave nao pode ser vazia.")

    # Soma o valor ASCII de cada letra da chave
    soma_ascii = 0
    for letra in chave:
        soma_ascii = soma_ascii + ord(letra)

    return soma_ascii


def criptografar(mensagem, chave):

    # Converte a chave de texto para um número
    chave_numerica = calcular_chave_numerica(chave)
    codigos = []

    for caractere in mensagem:
        # Converte cada caractere da mensagem para número
        
        codigo_ascii = ord(caractere)
        print(f"Código ASCII de {caractere} é :{codigo_ascii}")

        # codigo_criptografado = ord(caractere) + chave_numerica
        codigo_criptografado = codigo_ascii + chave_numerica

        codigos.append(codigo_criptografado)

    return codigos


def descriptografar(codigos, chave):
    # Usa a mesma chave numérica para desfazer a criptografia
    chave_numerica = calcular_chave_numerica(chave)
    mensagem = []

    for codigo in codigos:
        # Descriptografia: subtrai a mesma chave numérica
        codigo_original = codigo - chave_numerica

        # Transforma o número de volta em caractere
        mensagem.append(chr(codigo_original))

    return "".join(mensagem)


def listar(codigos):
    # Mostra os códigos já criptografados
    if len(codigos) == 0:
        print("Nao ha codigos para mostrar.")
        return

    print("Codigos criptografados:")
    for codigo in codigos:
        print(codigo, end=" ")
    print()


'''def listar_codigos(codigos):
    listar(codigos)'''


def main():
    # Vou usar a lista global dentro da função
    global lista_codigos

    print("--- Criptografia ASCII com Chave String ---")
    mensagem = input("Introduza a mensagem: ")
    chave = input("Introduza a chave: ")

    # try/except evita que o programa "quebre" se a chave for inválida
    try:
        chave_numerica = calcular_chave_numerica(chave)
        lista_codigos.clear()
        lista_codigos.extend(criptografar(mensagem, chave))
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    print(f"Chave numerica: {chave_numerica}")
    listar(lista_codigos)
    mensagem_original = descriptografar(lista_codigos, chave)
    print(f"Mensagem descriptografada: {mensagem_original}")


if __name__ == "__main__":
    # Executa o programa só quando este ficheiro é corrido diretamente, achei boa prática aplicar :)
    main()
