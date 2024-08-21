import os
os.system("cls")

sex = int(input("Digite seu sexo (Feminino: 1 / Masculino: 2): "))
height = int(input("Digite sua altura em cm: "))

match sex:
    case 1:
        weight = (62.1 * height) - 44.7
        print("Seu peso ideal é: ", weight)
    case 2:
        weight = (72.7 * height) - 58
        print("Seu peso ideal é: ", weight)
    case _:
        print("Sexo não registrado!")
