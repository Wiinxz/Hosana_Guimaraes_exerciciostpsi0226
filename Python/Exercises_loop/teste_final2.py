'''
Elabore uma base de dados de clientes de uma fábrica de materiais.

O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ).
Divida final=compra - desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. 
 
 O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente.
'''

clients = []
counter_id = 1

# def para menu - OK
# def para add cliente - OK
# def para inserir desconto -OK
# def para buscar cliente por numero - OK
# def para ver listagem completa - OK
 
def menu ():
 
 print("-------- Fábrica de matériais --------")
 print("Choose an option\n")
 print("[1] - Add costumer and purchase")
 print("[2] - Looking for costumers")
 print("[3] - View all costumers who have made purchases")
 print("[0] - Exit")

 option_menu = int(input())

 return option_menu

def add_client ():
 
 
 
 name = input("Enter the customer's name: ")
 address = input("Enter the customer's address:")
 phone = input("Enter the customer's phone number:")
 nif = input("Enter the customer's NIF: ")
 purchase_client = float(input("Enter the customer's purchase: "))
 discout = insert_discount(purchase_client)
 div_fin = purchase_client - discout


 new_cliente = {
  "Númcli": counter_id ,
  "NomCli": name,
  "Morada": address,
  "Tel": phone,
  "NIF": nif,
  "Compra": purchase_client,
  "Divfin": div_fin,
 }

 clients.append(new_cliente)

 counter_id = counter_id + 1

 return new_cliente  

def insert_discount(purchase):
  
  apply_discout = 0.0

  if purchase >= 100 and purchase <= 200:
    apply_discout = purchase * 0.05

  elif purchase >= 201 and purchase <= 499:
   apply_discout = purchase * 0.10 
 
  elif purchase >=500:
   apply_discout = purchase * 0.15

  return apply_discout

def look_all_costumers():
 
 for i in clients:
   print(f"ID CLIENT: ", i["Númcli"])
   print(f"NAME: ",i["NomCli"])
   print(f"ADDRESS: ",i["Morada"])
   print(f"PHONE NUMBER: ",i["Tel"])
   print(f"NIF: ",i["NIF"])
   print(f"PURCHASE VALUE: ",i["Compra"])
   print(f"FINAL PURCHASE VALUE WITH DISCOUNT APPLIED: ",i["Divfin"])
  
def search_by_phone():
    find = False
    search_phone = input("Enter the phone number : ")
    
    for i in clients:

        if i["Tel"] == search_phone:
            print("ID CLIENT: ", i["Númcli"])
            print("NAME: ", i["NomCli"])
            print("ADDRESS: ", i["Morada"])
            print("PHONE NUMBER: ", i["Tel"])
            print("NIF: ", i["NIF"])
            print("PURCHASE VALUE: ", i["Compra"])
            print("FINAL PURCHASE VALUE WITH DISCOUNT APPLIED: ", i["Divfin"])
            find = True

    if not find:
        print("This phone number is not listed !")

program_on = True

while program_on == True:
 
 option_menu = menu() 


 if option_menu != 1 and option_menu!=2 and option_menu!= 3 and option_menu != 0: 
  print("CHOOSE A VALID OPTION !!!")
  continue
 

 match option_menu:
  
  case 1 : 
    add_client()
    print("Client added successfully :) \n")

  case 2:
    search_phone = search_by_phone()

  case 3: look_all_costumers()

  case 0:
     print("Goodbye :) ")
     program_on = False
   
   
   
  
   

