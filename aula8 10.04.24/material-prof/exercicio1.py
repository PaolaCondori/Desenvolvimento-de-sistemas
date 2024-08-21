# --------------- SUBALGORITMOS
def preenche_vetor(l: list) -> None:
    while True:
        elem = input("Elemento:")
        if elem != '.':
            l.append(elem)
        else:
            break


# --------------- PROGRAMA PRINCIPAL
lista = []
preenche_vetor(lista)
print(f"Lista = {lista}")

"""
1. Tranforme esta rotina em um procedimento.
2. Fazer um programa que pegue o indice e o elemento e insira-o na lista.
"""