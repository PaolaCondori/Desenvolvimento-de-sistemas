import os
os.system("cls")

def soma_elementos() -> int:
    soma = 0
    for i in range(5):
        soma += v[i]
    return soma

def media_elementos() -> float:
    return soma_elementos()/5

v = [45, -89, 32, -12, 33]
x = media_elementos()
print(f"\nMédia dos elementos do vetor é: {x}")