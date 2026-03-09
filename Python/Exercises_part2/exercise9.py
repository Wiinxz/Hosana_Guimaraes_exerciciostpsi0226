'''
Processamento de requisição

Recebe um dicionário com as chaves "metodo" e "conteudo".

Retorna:
•	“Requisição GET recebida” se o método for “GET”
•	“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
•	“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
•	“Método não suportado” caso contrário

'''

requisicao = {"metodo": "GET", "conteudo": " "}

match(requisicao):
    
    case _ if requisicao["metodo"] == "POST" :
        
        if requisicao.get("conteudo") == "":
         print("Requisição POST sem dados")
        
        else:
           print("Requisição POST com dados válidos")
    
    
    case _ if requisicao["metodo"] == "GET":
      
      print("Requisição recebida")
    
    case _ :
      print("Método não suportado")

    

    