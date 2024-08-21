import os
os.system("cls")

"""Fazer uma função chamada ‘conta_inteiro(l)’ 
que conte quantos elementos inteiros existem em uma lista."""

def conta_inteiro(l: list) -> int:
    cont = 0
    cont2 = 0

    for i in l:
       cont += 1

    for j in range(cont):
        if type(l[j]) == int:
            cont2 += 1

    return cont2

lista = [4, 8, "DS", True, 78, 'P', 45.5]
x = conta_inteiro(lista)

print(f"\nO número de elementos inteiros na lista {lista} é {x}")