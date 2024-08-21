import os
os.system("cls")
def ordena() -> None:
    print(f"v = {v}")
    h = 0
    for i in range(4):
        for j in range(i+1, 5):
            if v[i] > v[j]:
                h = v[i]
                v[i] = v[j]
                v[j] = h
    print(f"\nO vetor em ordem crescente é: {v}")
                
v = [45, -89, 32, -12, 33]
ordena()