import os 
import exercicios

ent = 1

while ent == 1:
    os.system("cls")
    print("====== Menu ======")
    print('''\n1- Adiciona elementos a uma list até a tecla .\t\t\t\t\t4- Exibe o índice do elemento recebido\n2- Exibe lista\t\t\t\t\t\t\t\t\t5- Quantas vezes elemento aparece na lista\n3- Indica a quantidade de elementos na list\t\t\t\t\t6- Indica a quantidade de números inteiros na lista\n\t\t\t\t\t\t\t\t\t\t0- Sair''')
    opc = int(input("Digite uma das opções: "))

    while opc < 0 or opc > 6:
        opc = int(input("Tente novamente! Digite uma das opções válidas: "))
        match opc:
            case 0:
                print("\nObrigada por utilizar o programa!")
                break
            case 1:
                os.system("cls")
                lista = []
                exercicios.preenche_lista(lista)
                ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

            case 2:
                os.system("cls")
                lista = [2, 4, 6 ,7]
                exercicios.exibe_lista(lista)
                ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

            case 3:
                os.system("cls")

                lista = [1,2,3,4,5,6]
                x = exercicios.conta_elementos(lista)
                print(f"O número de elementos na lista {lista} é igual a {x}")
                ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

            case 4:
                os.system("cls")
            
                lista = [7, 89, 4, 29, 10]
                elemento = int(input("Insira um elemento: "))

                x = exercicios.retorna_indice(elemento)
                if x == -1:
                    print(f"\nValor {elemento} não encontrado na lista\nRetorno: {x}")
                else:
                    print(f"\nValor encontrado, o índice do elemento {elemento} é {x}")
                ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

            case 5:
                os.system("cls")

                lista = [22, 22, 57, 3, 3, 3]
                elemento = int(input("Digite o elemento inteiro: "))

                x = exercicios.busca(lista, elemento)

                if x == -1:
                    print(f"\nValor {elemento} não encontrado na lista\nRetorno: {x}")
                else:
                    print(f"\nO número de vezes que o elemento {elemento} aparece na lista é {x}")
                ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

            case 6:
                os.system("cls")

                lista = [4, 8, "DS", True, 78, 'P', 45.5]
                x = exercicios.conta_inteiro(lista)

                print(f"\nO número de elementos inteiros na lista {lista} é {x}")
                ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))
    else:
        os.system("cls")
        print("Obrigada por utilizar o programa!")