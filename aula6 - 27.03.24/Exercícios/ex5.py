import  os
os.system("cls")

def elementos_impares() -> None:
    print("\nOs elementos ímpares do vetor são:")
    for i in range(5):
        if v[i]%2 != 0:
            print(v[i])


v = [45, -89, 32, -12, 33]
elementos_impares()