import os

def preenche_lista(l: list) -> None:
    print("\nAdicione elementos em uma lista, pressione a tecla . para encerrar o programa")
    while True:
        elemento = input("Elemento: ")
        if elemento == '.':
            break
        else:
            l.append(elemento)
    print(f"\nObrigada por utilizar o programa!\nResultado da lista: Lista = {l}")

lista = []
preenche_lista(lista)