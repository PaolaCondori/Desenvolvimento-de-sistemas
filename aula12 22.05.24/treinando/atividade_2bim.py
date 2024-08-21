import os
os.system("cls")

#Função
def placa(s : str) -> bool:
0,    letras= "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    carac = "@*&$#_+!?"
    cont = 0
    result = True

    for i in range(len(s)):
        cont += 1
        if s[i] in carac:
            result = False
            break
        

    if cont == 7:
        for i in range(0, 4, 1):
            if s[i] not in letras:
                result = False
                break
            else:
                result = True
        
        if s[3] or s[5] or s[6] not in numeros:
            result = False
        else:
            result = True

        if s[4] not in letras:
            result = False
        else:
            result = True  
    else:
        result = False
        
    return result
        
#programa principal
print(placa("abc5d67")) #True
print(placa("abc5d6")) #False
print(placa("1234567")) #False
print(placa("abc5d678")) #False
print(placa("ab@5d678")) #False
print(placa("abc@d67")) #False
print(placa("aBC5d67")) #True
