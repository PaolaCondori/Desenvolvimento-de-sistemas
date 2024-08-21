import os
os.system("cls")

frase = input("Frase: ")
c1 = input("Caractere a ser localizado: ")
c2 = input("Trocar pelo caractere: ")

print(f"\n{frase.replace(c1, c2)}")