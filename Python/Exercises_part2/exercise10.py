'''
 Jogo: Pedra, Papel ou Tesoura

Cria um programa que receba duas jogadas:
•	Jogador 1
•	Jogador 2

Usa match para determinar o resultado:
•	Pedra ganha de Tesoura
•	Tesoura ganha de Papel
•	Papel ganha de Pedra
•	Se forem iguais, é Empate

Exemplo:
Entrada →
Jogador 1: pedra
Jogador 2: tesoura
Saída → Jogador 1 venceu

'''

print("Jogo: Pedra, Papel ou Tesoura xD")

gamer1 = input("\nJogador 1 insira sua jogada: ").lower()
gamer2 = input("Jogador 2 insira sua jogada: ").lower()

match (gamer1, gamer2):

    case _ if gamer1 == gamer2:
        print("Empate!")

    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu!")

    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu!")

    case _:
        print("Jogada inválida")

