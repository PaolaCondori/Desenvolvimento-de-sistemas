import os
os.system("cls")

def ordena_vetor_decrescente() -> None:
    h = 0
    print(f"\nv1 = {v1}")
    for i in range(4):
        for j in range(i + 1, 5):
            if v1[i] < v1[j]:
                h = v1[i]
                v1[i] = v1[j]
                v1[j] = h
    print(f"\nO vetor em ordem decrescente é: {v1}")


v1 = [41, 72, 39, 4, 35]
ordena_vetor_decrescente()