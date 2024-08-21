import os 

os.system("cls")

passwd = int(input("Digite a senha para acessar o computador: "))

passwdSystem = 1234

if passwd == passwdSystem:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")