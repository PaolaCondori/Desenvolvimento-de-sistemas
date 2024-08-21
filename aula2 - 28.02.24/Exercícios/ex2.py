import os

os.system("cls")

year = int(input("Digite o ano que você nasceu: "))

age = 2024 - year

if age >= 16:
    print("Você já pode votar em 2024")
else:
    print("Você ainda não pode votar em 2024")