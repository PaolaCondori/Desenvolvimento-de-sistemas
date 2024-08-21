import os

os.system("cls")

apple = int(input("Digite o número de maçãs compradas: "))

if apple < 12:
    priceShop = apple * 0.3
    print("Valor da compra: R$" , priceShop)
else:
    priceShop = apple * 0.25
    print("Valor da compra: R$", priceShop)