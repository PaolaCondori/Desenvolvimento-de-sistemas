import os
os.system("cls")

def busca(n: int) -> bool:
    for i in range(5):
        if n == v[i]:
            return True
    else:
        return False

v = [45, -89, 32, -12, 33]
n = int(input("\nDigite um valor: "))

x = busca(n)
if x == True:
    print(f"O resultado é {x} porque existe o elemento {n} no vetor")
else:
    print(f"O resultado é {x} porque não existe o elemento {n} no vetor")

