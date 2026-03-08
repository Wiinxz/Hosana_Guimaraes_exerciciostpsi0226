'''
Classificação de produto

Recebe um dicionário com as chaves "categoria" e "preco".
Retorna:
•	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
•	“Produto comum” se categoria for “eletrônico” e preço até 1000
•	“Produto alimentar” se categoria for “alimento”
•	“Categoria desconhecida” caso contrário

Exemplo:
Entrada → {"categoria": "eletrônico", "preco": 1500}
Saída → Produto de luxo

'''

produto = {"categoria": "eletronico", "preco": 5000}

match(produto):

    case _ if produto["categoria"] == "eletronico":
      
        if produto["preco"] > 1000:
            print("Produto de luxo")
        else:
            print("Produto comum")
    
    case _ if produto["categoria"] == "alimento":
        print("Produto Alimentar")
    
    case  _ :
        print("Categoria desconheçida")
