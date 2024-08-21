import os
os.system("cls")

nSides = int(input("Digite o número de lados de um polígono regular: "))
cmSide = int(input("Digite a medida do lado em cm: "))

if nSides == 3:
    area = (cmSide * cmSide) / 2
    print("TRIÂNGULO - Área: ", area, "cm²")
elif nSides == 4:
    area = cmSide * cmSide
    print("QUADRADO - Área: ", area, "cm²")
elif nSides == 5:
    print("PENTÁGONO")
elif nSides < 3:
    print("NÃO É UM POLÍGONO")
elif nSides > 5:
    print("POLÍGONO NÃO IDENTIFICADO")