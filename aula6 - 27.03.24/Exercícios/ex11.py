import os
os.system("cls")
def inverte_vetor() -> None:
    for i in range(5):
        v2[4-i] = v1[i]
    print(f"v1 = {v1}\n\nResultado da inversão de v1 em v2:\nv2 = {v2}")

v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
inverte_vetor()