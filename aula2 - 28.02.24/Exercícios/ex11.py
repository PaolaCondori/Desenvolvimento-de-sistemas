import os
os.system("cls")

side1 = int(input("Digite a medida do primeiro lado: "))
side2 = int(input("Digite a medida do segundo lado: "))
side3 = int(input("Digite a medida do terceiro lado: "))

if side1 == 90 or side2 == 90 or side3 == 90:
    print("É um TRIÂNGULO RETÂNGULO")
elif side1 > 90 or side2 > 90 or side3 > 90:
    print("É um TRIÂNGULO OBTUSÂNGULO")
elif side1 < 90 and side2 < 90 and side3 < 90:
    print("É um TRIÂNGULO ACUTÂNGULO")