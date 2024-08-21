import os
os.system("cls")

def soma_elementos() -> int:
    soma = 0
    for i in range(5):
        soma += v[i]
    return soma

v = [45, -89, 32, -12, 33]
x = soma_elementos()

print(f"\nSoma dos elementos do vetor é: {x}")