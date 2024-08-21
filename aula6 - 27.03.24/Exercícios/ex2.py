import os
os.system("cls")

def exibe_negativo() -> None:
    print("\nOs elementos negativos do vetor são: ")
    for i in range(5):
        if v[i] < 0:
            print(v[i])

v = [45, -89, 32, -12, 33]
exibe_negativo()