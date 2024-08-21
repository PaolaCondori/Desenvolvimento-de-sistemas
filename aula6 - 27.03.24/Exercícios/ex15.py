import os
os.system("cls")

def separa_pares_impares() -> None:
    print(f"\nv1 = {v1}")
    h = 0
    for i in range(4):
        for j in range(i + 1, 5):
            if v1[i] % 2 != 0:
                h = v1[i]
                v1[i] = v1[j]
                v1[j] = h
    print(f"\nResultado da separação dos elementos pares e ímpares: {v1}")

v1 = [41, 72, 39, 4, 35]
separa_pares_impares()