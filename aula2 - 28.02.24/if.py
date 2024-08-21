#Importar uma biblioteca, a os. Sistema operacional
import os

#Tipos de if no python

"""
Sintaxe if composto em pyhton:

idade = int(input("Idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
"""

"""
Sintaxe if simples

numero = int(input("Numero: "))

if numero < 0:
    numero = numero * -1

print("Numero: {numero}")
"""

"""
Sintaxe if encadeado

numero = int(input("Numero: "))

if numero < 0:
    print("Negativo")
else:
    if numero > 0:
        print("Positivo")
    else:
        print("Nulo")
"""

"""
Sintaxe elif (faz a mesma coisa que um if encadeado, deixa o código menor)

numero = int(input("Numero: "))

if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Nulo")
"""

#Comando switch em python

os.system("cls")

print("""
1- Enunciando exercício 1
2- Enunciando exercício 2
3- Enunciando exercício 3
4- Enunciando exercício 4
    """)

opcao = int(input("Numero: "))

#switch do pyhton
match opcao:
    case 1:
        print("Executando exercício 1")

    case 2:
        print("Executando exercício 2")

    case 3:
        print("Executando exercício 3")

    case 4:
        print("Executando exercício 4")

    #serve como o default
    case _:
        print("ERRO")