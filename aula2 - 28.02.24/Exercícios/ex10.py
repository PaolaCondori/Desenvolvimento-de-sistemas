import os
os.system("cls")

side1 = int(input("Digite a medida do primeiro lado: "))
side2 = int(input("Digite a medida do segundo lado: "))
side3 = int(input("Digite a medida do terceiro lado: "))

if side1 == side2 and side1 == side3:
    print("O triângiulo é EQUILÁTERO")
elif side1 == side2 and side1 != side3:
    print("O triângulo é Isóceles")
elif side1 == side3 and side1 != side2:
    print("O triângulo é Isóceles")
elif side2 == side3 and side2 != side1:
    print("O triângulo é Isóceles")
else:
    print("O triânglo é ESCALENO")