import os
os.system("cls")

def maior_elemento() -> int:
    h = 0
    for i in range(5):
        if v1[i] > h:
            h = v1[i]
    return h

v1 = [41, 72, 39, 4, 35]
print(f"\nv1 = {v1}")
x = maior_elemento()
print(f"\nO maior elemento do vetor é: {x}")