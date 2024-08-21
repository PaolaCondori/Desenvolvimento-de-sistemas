import os
os.system("cls")

l =  ["Edson", 12, 1.67, True, 34]
print(f"\nExibe a posição 1 da lista: L[1]  = {l[1]}")
print(f"\nExibe a lista inteira: L = {l}")

l[0] = 10
print(f"\nL = {l}")

lista = list()
#append -> adiciona um dado no final da lista
lista.append(22)
lista.append("Lógica")
print(lista)

#insert -> insere um dado numa posição da lista,empurrando o elemento antes presente, possui 2 param.,
# insert(index, conteúdo)
lista.insert(1, 57.7)
print(lista)

#pop -> remove o elemento com o index passado por param.
#Sem param. remove o último valor
lista.pop(0)
print(lista)
lista.pop()
print(lista)

#remove -> remove o elemento com o valor passado por param.
lista.remove(57.7)
print(lista)

""""lista.remove(30)
print(lista)"""

lista = [22, 57.7, "Lógica"]
#index -> retorna o index do valor passado por param.
indice = lista.index("Lógica")
print(f"índice = {indice}")

"""indice = lista.index(30)
print(f"{indice}")"""

lista = [22, 22, 57.7, "Lógica"]
#count -> retorna a quantidade de elementos passado por param.
qtd = lista.count(22)
print(f"Quantidade = {qtd}")

qtd = lista.count(30)
print(f"Quantidade = {qtd}")

#len -> retorna a quantidade de elementos da lista, é uma função
qtd_elementos = len(lista)
print(f"Quantidade = {qtd_elementos}")

lista = [19, 4, 25, 33, -5]
#sum -> soma os elementos de uma lista numérica, se encontrar um valor que não seja numérico quebra (é função)
print(sum(lista))

"""lista = [19, 4, 25, 33, -5, "Lógica"]
print(sum(lista))"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
#+ -> concatena listas
#lista3 = lista1 + lista2
lista2 = lista1 + lista2
lista3 = lista2 + lista1
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")
print(f"Lista3 = {lista3}")

#extend -> adiciona no final da lista outra lista passada por param.
lista2.extend(lista1)
print(f"Lista2 = {lista2}")

#copy -> copia valores de uma lista em outra
lista2 = lista1.copy()
print(f"Lista1 = {lista1}")
print(f"Lista2 = {lista2}")

lista1 = lista2
lista1.append(4)

print(lista1, lista2)

lista = [19, 4, 25, 33, -5]
#sort -> ordena elementos de uma lista em ordem crescente
lista.sort()
print(lista)

#sort(reverse=True) -> ordena os elementos de uma lista em ordem decrescente
lista.sort(reverse=True)
print(lista)

#reverse -> inverte os elementos da lista
lista.reverse()
print(lista)

lista.clear()
print(lista)

del(lista)
#print(lista)