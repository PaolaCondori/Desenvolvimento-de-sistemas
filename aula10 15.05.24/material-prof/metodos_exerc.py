import os 
os.system("cls")
#Lista -> dados heterogeneos, no caso diversos tipos de dados, como int, char, float etc, com tamanho dinâmico
#Vetor -> dados homogeneos, apenas um tipo de dado, como um vetor apenas com inteiros, além de ter seu temanho pré-definido

#Para criar vetor
vetor = [1, 2, 3, 4, 5, 6]
vetor = [] #-> vetor vazio

#Para criar uma lista
l = list()
lista = [1, 2, 3, 4, 5, 6]

#Métodos de uma lista

#-> append: adiciona um elemento no final da lista
lista.append("SKZ")
print(lista)

#-> insert: adiciona um elemento na lista empurrando para frente o index colocado com parametro
#Sintaxe -> lista.insert(index empurrado, elemento inserido)
lista.insert(6, "Chan")
print(lista)

#-> index:  mostra o index do elemento passado por parametro, se coloca em uma variavel
indice = lista.index(5)
print(f"indice = {indice}")

#-> pop: retira o último elemento da lista quando esta sem parametro, mas com parametro ele retira o index passado por param. 
lista.pop()
print(lista)

lista.pop(1)
print(lista)

#-> sort: ordena elementos da lista em ordem crescente
lista2 = [25, 3, 8, 8]
lista2.sort()
print(lista2)

#mostra a lista de forma decrescente
lista2.sort(reverse=True)
print(lista2)
#-> Remove: remove o elemeto passado por parametro
lista2.remove(25)
print(lista2)

#-> Count: conta a quantidade de vezes que o elemento aparece na lista, para ver é necessário aramzená-lo em uma variável
qtd = lista2.count(8)
print(qtd)

#-> Copy: copia valores de uma lista em outra lista, para isso é necessário:
#-> sintaxe: lista que vai copiar = lista que é copiada, inclusive agr elas podem ser modificadas da mesma maneira, se uma é modifcada a outra tbm é
lista = lista2.copy()
print(f"lista1: {lista}")
print(f"lista2: {lista2}")

#-> Reverse: inverte os elementos da lista 
lista.reverse()
print(lista)


#-> extend: adiciona no final de uma lista outra lista
lista2.extend(lista)
print(lista2)

#-> Clear: limpa toda lista
lista2.clear()
#print(lista2)

#-> len: é uma função que conta quantos elementos possuem uma lista
qtd_elem = len(lista)
print(f"qtd_elem = {qtd_elem}")


print(sum(lista))

del(l)

#-> Clear: limpa toda lista
lista2.clear()
#print(lista2)


#Métodos de um vetor de Char: String (string não é um tipo dado, é um objeto)

#-> string.find("elemento"): procura elemneto passado por parametro, se n encontra retorna -1 

#-> .join(lista string): transforma lista de strings em apenas uma vetor com uma string

#-> string.strip(): transforma uma lista string em uma uma lsita com strings, sem param. ele separa por espaço, contrario join 

#-> string.split():elimina espaços antes e depois da string

#-> string.replace('subtituir', subtituto): substitui um elemntos de uma string por outro, ex: e por E
