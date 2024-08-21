import os

opcao = 1

while opcao == 1:
    os.system("cls")
    print("""
    Menu Python
    1- Maior número
    2- Eleição 2024
    3- Senha computador
    4- Compra de maçãs
    5- Ordem crescente
    6- Peso ideal
    7- Polígono regular
    8- Polígono regular pt2
    9- Maior número pt2
    10- Tipo triângulo
    11- Tipo triângulo pt2
    12- Número primo
    0- Sair
    """)

    opcao = int(input("Digite uma das opções: "))
    
    match opcao:
        case 0:
            break

        case 1:
            os.system("cls")

            n1 = int(input("Digite um número: "))
            n2 = int(input("Digite outro número: "))

            if n1 > n2:
                print("O maior número é: ", n1)
            else:
                print("O maior número é: ", n2)
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        
        case 2:
            os.system("cls")

            year = int(input("Digite o ano que você nasceu: "))

            age = 2024 - year

            if age >= 16:
                print("Você já pode votar em 2024")
            else:
                print("Você ainda não pode votar em 2024")
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))

        case 3:
            os.system("cls")

            passwd = int(input("Digite a senha para acessar o computador: "))

            passwdSystem = 1234

            if passwd == passwdSystem:
                print("ACESSO PERMITIDO")
            else:
                print("ACESSO NEGADO")
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 4:
            os.system("cls")

            apple = int(input("Digite o número de maçãs compradas: "))

            if apple < 12:
                priceShop = apple * 0.3
                print("Valor da compra: R$" , priceShop)
            else:
                priceShop = apple * 0.25
                print("Valor da compra: R$", priceShop)
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 5:
            os.system("cls")

            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            n3 = int(input("Digite o terceiro número: "))

            if n1 > n2 and n2 > n3:
                print("Ordem crescente: ", n3, n2, n1)
            elif n1 > n3 and n3 > n2:
                print("Ordem crescente: ", n2, n3, n1)
            elif n2 > n1 and n1 > n3:
                print("Ordem crescente: ", n3, n1, n2)
            elif n2 > n3 and n3 > n1:
                print("Ordem crescente: ", n1, n3, n2)
            elif n3 > n1 and n1 > n2:
                print("Ordem crescente: ", n2, n1, n3)
            elif n3 > n2 and n2 > n1:
                print("Ordem crescente: ", n1, n2, n3)
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 6:
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
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 7:
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
            else:
                print("Polígono não registrado")
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 8:
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
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 9:
            os.system("cls")

            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            n3 = int(input("Digite o terceiro número: "))

            if n1 > n2 and n1 > n3:
                print("O maior número é: ", n1)
            elif n2 > n1 and n2 > n3:
                print("O maior número é: ", n2)
            elif n3 > n1 and n3 > n2:
                print("O maior número é: ", n3)
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 10:
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
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 11:
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
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case 12:
            os.system("cls")

            num = int(input("Digite um número: "))
            total = 0

            for c in range(1, num+1):
                if num%c==0:
                    total+=1
            if total==2:
                print("O número {} é primo!".format(c))
            else:
                print("O número {} não é primo!".format(c))
            opcao = int(input("\nDigite 0 para sair ou 1 para voltar ao menu: "))
        case _:
            print("Opção inválida! Digite novamente")
            continue
        