import os
os.system("cls")
def transformaVogalMaiuscula(l: str) -> str:
    vogais = "aeiou"
    for i in range(0, len(l), 1):
        if l[i] in vogais:
            l = l.replace(l[i], l[i].upper())
    return print(l)
        
lista = ("Dia 30 eh meu niver")
transformaVogalMaiuscula(lista)

