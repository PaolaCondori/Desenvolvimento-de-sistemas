import os
os.system("cls")

def exibe_indice_impar() -> None:
    print("\nOs elementos com índices ímpares são:")
    for i in range(5):
        if i%2 != 0:
            print(v[i])

v = [45, -89, 32, -12, 33]
exibe_indice_impar()