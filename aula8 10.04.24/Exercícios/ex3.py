import os
os.system("cls")

def conta_elementos(l: list) -> int:
    cont = 0
    for i in l:
        cont +=1
    return cont

lista = [1,2,3,4,5,6]
x = conta_elementos(lista)
print(f"O número de elementos na lista {lista} é {x}")