#1. Fazer um procedimento que passe uma string por parâmetro e transofrme todas as vogais em maiusculo
import os
os.system("cls")

def letra_maiuscula(frs: str, inter: str) -> None:
    for i in range(len(frs)):
        if frs[i] in inter:
            frs = frs.replace(frs[i], frs[i].upper())
    print(frs)

frase = "Hoje eu quero ir pra casa no almoçu"
vogais = "aeiou"
letra_maiuscula(frase, vogais)