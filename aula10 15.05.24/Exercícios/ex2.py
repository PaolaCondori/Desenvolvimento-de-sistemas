#2. Faca uma função que passe uma lista por parâmetro e retorne True caso todos sejam inteiros, senao false
import os
os.system("cls")

def check_int_list(l: list) -> bool:
    transform_list_str(l)
    numbers = "0123456789"
    cont = 0
    list_test = False
    for i in range(len(l)):
        if l[i] in numbers:
            list_test = True
        elif not l[i] in numbers:
            if l[i] == '-' or l[i] == '+':
                list_test = True
            else:
                return list_test
                break
    
    return list_test
    

def transform_list_str(l: list) -> None:
    for i in range(len(l)):
        l[i] = str(l[i])


lista = [1, 6, 90, 2.9, "DS", False]
lista2 = [-7, 9, 34, 2, 5]
x = check_int_list(lista2)
print(x)