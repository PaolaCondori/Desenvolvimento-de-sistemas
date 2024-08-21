import os
os.system("cls")
def retorna_indice(elem: int) -> int:
    cont = 0
    for i in lista:
        cont += 1

    for j in range(cont):
        if lista[j] == elem:
            return j
    else:
        return -1


lista = [7, 89, 4, 29, 10]
elemento = int(input("Insira um elemento: "))

x = retorna_indice(elemento)
if x == -1:
    print(f"\nValor {elemento} não encontrado na lista\nRetorno: {x}")
else:
    print(f"\nValor encontrado, o índice do elemento {elemento} é {x}")