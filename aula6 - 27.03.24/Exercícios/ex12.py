import os
os.system("cls")

def ordena_vetor_crescente() -> None:
    print(f"\nv1 = {v1}")
    h = 0
    for i in range(4):
        for j in range(i+1, 5):
            if v1[i] > v1[j]:
                h = v1[i]
                v1[i] = v1[j]
                v1[j] = h
    print(f"\nO vetor em ordem crescente é: {v1}")

v1 = [41, 72, 39, 4, 35]
ordena_vetor_crescente()