lista1 = []
lista2 = [2, 4, 6 ,7]
lista3 = [1,2,3,4,5,6]
lista4 = [7, 89, 4, 29, 10]


def preenche_lista(l: list) -> None:
                print("\nAdicione elementos em uma lista, pressione a tecla . para encerrar o programa")
                while True:
                    elemento = input("Elemento: ")
                    if elemento == '.':
                        break
                    else:
                        l.append(elemento)
                print(f"\nResultado da lista: Lista = {l}")


 def exibe_lista(l: list) -> None:
        print(f"\nLista = {l}")


 def conta_elementos(l: list) -> int:
                cont = 0
                for i in l:
                    cont +=1
                return cont


 def retorna_indice(elem: int) -> int:
                cont = 0
                for i in lista:
                    cont += 1

                for j in range(cont):
                    if lista[j] == elem:
                        return j
                else:
                    return -1


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


def conta_inteiro(l: list) -> int:
                cont = 0
                cont2 = 0

                for i in l:
                    cont += 1

                for j in range(cont):
                    if type(l[j]) == int:
                        cont2 += 1
                