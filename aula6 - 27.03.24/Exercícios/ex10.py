import os
os.system("cls")

def copia_vetor() -> None:
    print(f"v1 = {v1}")
    for i in range(5):
        v2[i] = v1[i]
    print(f"\nResultado da cópia de v1 --> v2\nv2 = {v2}")

v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

copia_vetor()