import os

op = 1

while op == 1:
    os.system("cls")
    print("\n------------------------------- Menu Vetor -------------------------------")
    print("\n1- Primeiro elemento\t\t\t\t\t10- Copiar vetor\n2- Números negativos\t\t\t\t\t11- Inverte vetor\n3- Soma elementos\t\t\t\t\t12- Ordem crescente\n4- Media elementos\t\t\t\t\t13- Ordem decrescente\n5- Números ímpares\t\t\t\t\t14- Ordem C ou D\n6- Primeiro e último elemento\t\t\t\t15- Separa pares\n7- Índices pares\t\t\t\t\t16- Conta acima da média\n8- Valor do vetor\t\t\t\t\t17- Maior elemento\n9- Ordebar elementos\t\t\t\t\t0- Sair")

    op2 = int(input("\nResposta: "))
    while op2 < 0 or op2 > 17:
        op2 = int(input("\nOpção inválida! Tente novamente: "))

    match op2:
        case 1:
            os.system("cls")
            from ex1 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 2:
            os.system("cls")
            from ex2 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 3:
            os.system("cls")
            from ex3 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 4:
            os.system("cls")
            from ex4 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 5:
            os.system("cls")
            from ex5 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 6:
            os.system("cls")
            from ex6 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 7:
            os.system("cls")
            from ex7 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 8:
            os.system("cls")
            from ex8 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 9:
            os.system("cls")
            from ex9 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 10:
            os.system("cls")
            from ex10 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 11:
            os.system("cls")
            from ex11 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 12:
            os.system("cls")
            from ex12 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 13:
            os.system("cls")
            from ex13 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 14:
            os.system("cls")
            from ex14 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 15:
            os.system("cls")
            from ex15 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 16:
            os.system("cls")
            from ex16 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 17:
            os.system("cls")
            from ex17 import *
            op = int(input("\nDeseja continuar no menu? [1]Sim [0]Não\nResposta: "))

        case 0:
            print("\nObrigada por utilizar o menu!")
            break

else:
    print("\nObrigada por utilizar o menu!")