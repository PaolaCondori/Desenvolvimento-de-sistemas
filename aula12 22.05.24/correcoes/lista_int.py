def eh_lista_int(l: list) -> bool: # [45, 33, 96]
    transforma_str(l) # [45, 33, 96]
    lista_int = True
    for i in range(len(lista)):
        if not l[i].isnumeric():
            lista_int = False
            

    return lista_int

def transforma_str(l: list) -> None: # [45, 33, 96]
    for i in range(len(l)):
        l[i] = str(l[i])
# ["45", "33", "96"]



# programa principal

lista = [45, 33, 96]
print(eh_lista_int(lista)) # True
lista = [45, "Edson", 96]
print(eh_lista_int(lista)) # False

x = "-345"
print(x.isnumeric())
