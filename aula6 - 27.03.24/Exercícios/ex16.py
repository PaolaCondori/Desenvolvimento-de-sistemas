import os

os.system("cls")

def soma_elementos() -> int:
    soma = 0
    for i in range(5):
        soma += v1[i]
    return soma


def conta_acima_media() -> int:
    cont = 0 
    x = soma_elementos()
    media = x/5
    for i in range(5):
        if v1[i] > media:
            cont += 1
    return cont

v1 = [41, 72, 39, 4, 35]
print(f"\nv1 = {v1}")
y = conta_acima_media()

print(f"\nO número de elementos acima da média do vetor é: {y}")