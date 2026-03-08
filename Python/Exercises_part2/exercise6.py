'''
Estado do servidor

Recebe um dicionário com as chaves "status" e "tempo_resposta".
Retorna:
•	“Servidor ativo” se o status for “ok”
•	“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
•	“Servidor indisponível” se o status for “erro”
•	“Estado desconhecido” caso contrário

Exemplo:
Entrada → {"status": "ok", "tempo_resposta": 350}
Saída → Servidor lento

'''

servidor = {"status":"ok", "tempo_resposta": 150}

# só entra se for realmente maior que 200
if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
  print("Servidor lento :( ")

elif servidor["status"] == "ok":
 print("Servidor ativo :) ")

elif servidor["status"] == "erro":
  print("Servidor indisponível xO ")

else:
  print("Status desconhecido ?")