import os
os.system("cls")

def listaInteiros(l: list) -> bool:
    #isnumeric. -> verifica se todos os elementos de uma var/lista são string e numericos
    #str. -> converte para string
    lista_int = True # variavel com valor pré-determinado
    listaString(l)
    for i in range(len(l)): #percorre todos os elementos da lista, sendo a quantidade de caracteres em l
        if not l[i].isnumeric() and (not "-" in l[i]) and (not "+" in l[i]): #se não for numerico, no caso todos os elementos sendo strings, mas sendo numeros
            lista_int = False #modifica valor da variavel 
    return lista_int # retorno da variavel que pode ter mudade ou não
       

"""
    transformo em str
    encontra/procura o - na lista

    retorna true
"""
def listaString(l: list) -> None:
    #passar por todos os elementos da lista
    for i in range(len(l)):
        l[i] = str(l[i])#transforma todos os elementos da lista em string

intPos = [1, 2, 3, 4, 5, 6, 7, 8]
intNeg = [-1, -2, +3, -4, -5, +6, +7]
naoInt = [1, 2, 3, "oii", 2, 4, "mds"]
print(listaInteiros(intNeg))
