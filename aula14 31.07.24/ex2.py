import os
os.system("cls")

def list_type(l: list) -> None:
    l_int = []
    l_float = []
    l_str = []
    l_bool = []
    simbolos = ".,"
    b = "TrueFalse"
    for i in range(len(l)): 
        print(l[i])
        if l[i].isnumeric():
            l_int.append(l[i])
        elif l[i] in b:
            l_bool.append(l[i])
        elif l[i].replace(".", "").isdigit():
            l_float.append(l[i])
        else:
            l_str.append(l[i])

    print(f"\nlista original: {l}\nlista int: {l_int}\nlista float: {l_float}\nlista string: {l_str}\nlista boolean: {l_bool}")

lista = []

print("Digite . para parar\n")
while True:
    i = input(": ")
    if i == ".":
        break
    else:
        lista.append(i)

list_type(lista)