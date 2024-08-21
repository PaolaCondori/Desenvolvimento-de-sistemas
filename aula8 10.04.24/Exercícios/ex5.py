import os
os.system("cls")
def busca(l: list, elem: int) -> int:
    cont = 0
    cont2 = 0
    for i in l:
        cont += 1

    for j in range(cont):
        if l[j] == elem:
            cont2 += 1
    else:
        if cont2 == 0:
            return -1
        else:
            return cont2

lista = [22, 22, 57, 3, 3, 3]
elemento = int(input("Digite o elemento inteiro: "))

x = busca(lista, elemento)

if x == -1:
    print(f"\nValor {elemento} não encontrado na lista\nRetorno: {x}")
else:
    print(f"\nO número de vezes que o elemento {elemento} aparece na lista é {x}")