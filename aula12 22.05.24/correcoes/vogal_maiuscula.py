    # Dada uma string converter as vogais em maiusculo
def vogal_miuscula_pros_fracos(s: str) -> str:
    s = s.replace("a", "A")
    s = s.replace("e", "E")
    s = s.replace("i", "I")
    s = s.replace("o", "O")
    s = s.replace("u", "U")
    return s

def vogal_miuscula_pros_fortes(s: str) -> str:
    vogal = "aeiou"
    for i in range(0, len(s), 1):
        if s[i] in vogal:
            s = s.replace(s[i], s[i].upper())
    return s

# programa principal
import os
os.system("cls")
texto = "Edson de Oliveira"
novo_texto = vogal_miuscula_pros_fracos(texto)
novo_texto2 = vogal_miuscula_pros_fortes(texto)
print(novo_texto)
print(novo_texto2)
