# ------- SUBALGORITMOS
def busca_elem_procedimento(l: list, elem: int) -> None: # parametro Formal
    encontrou = False
    for elemento in l:
        if elem == elemento:
            encontrou = True
            break

    if encontrou:
        print("Achou!")
    else:
        print("Não achou!")

def busca_elem_funcao(l: list, elem: int) -> bool: # parametro Formal
    encontrou = False
    for elemento in l:
        if elem == elemento:
            encontrou = True
            break

    return encontrou



# ------- PROGRAMA PRINCIPAL
import os
os.system("cls")
#        0  1   2  3  4   5
lista = [5, 9,  5, 0, 67, 5]

busca_elem_procedimento(lista, 99) # parametro Real
print()
if busca_elem_funcao(lista, 99):
    print("Achou!")
else:
    print("Não achou")

print()
'''
if lista.index(99) >= 0:
    print("Achou!")
else:
    print("Não achou")
'''
# lista.index(x[, start[, end]])
print(lista.index(5,3,6))