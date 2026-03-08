'''
Classificação de nota

Lê uma nota (0–100) e retorna uma classificação:
•	90 ou mais → Excelente
•	70–89 → Bom
•	50–69 → Suficiente
•	Abaixo de 50 → Insuficiente

Exemplo:
Entrada → 70-89
Saída →  Bom

'''
nota = int(input("Digite uma nota de 0 á 100 para ver sua classificação: "))

if nota < 50:
    print("Insuficiente :(")
elif nota <= 50 or nota <= 69:
    print("Suficiente :D ")
elif nota <= 70 or nota <= 89 :
    print("BOM !")
else :
    print("Excelente xD ")
