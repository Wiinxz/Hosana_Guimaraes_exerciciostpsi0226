'''
Análise de mensagem

Recebe uma mensagem e retorna:
•	“Saudação” se for “olá” ou “bom dia”
•	“Pergunta” se terminar com “?”
•	“Despedida” se contiver “tchau” ou “adeus”
•	“Mensagem genérica” caso contrário

Exemplo:
Entrada → “Tudo bem?”
Saída → Pergunta


'''

mensagem = input("Digite sua mensagem : ").lower()

match(mensagem):

    case _ if mensagem == "bom dia" or mensagem == "olá":
       print("Saudação")

    case _ if mensagem[-1] == "?":
        print("Pergunta") 

    #exercicio dizia "se contiver"
    case _ if "tchau" in mensagem or "adeus" in mensagem:
        print("Despedida")
    
    case _ : 
        print("Mensagem genérica")
  
