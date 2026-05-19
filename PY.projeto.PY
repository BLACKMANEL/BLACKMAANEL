while True:

 print("Boa tarde\n Barbearia Gonçalves\n")
 nome = input ("Qual e o seu nome ?")
 print (f"Bem-vindo", nome)

 data = list (range(1,32))
 dia = int(input("Qual data deseja marcar ? \n(ou 0 para sair): \n")) 
 if dia in data:
        print("DATA DISPONIVEL \n")
 else:
        print ("DATA INDISPONIVEL \n")  

 horarios = []
 for hora in range(8,21):
     for minuto in [0,30]:
       horarios.append(f"{hora:02d}:{minuto:02d}")
 print("HORARIOS")
 
 hora = (input("Digite um horario \n(ou 0 para sair )"))
 if hora in horarios:
    print(f" {nome} HORARIO DISPONIVEL ás {hora}")
 else:
    print(f" {nome} HORARIO INDIPONIVEL")    
 print(" OBRIGADO PELA PREFERENCIA !! ")
 break

