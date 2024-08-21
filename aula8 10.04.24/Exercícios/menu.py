import os 

ent = 1

while ent == 1:
    os.system("cls")
    print("====== Menu ======")
    print('''\n1- Adiciona elementos a uma list até a tecla .\t\t\t\t\t4- Exibe o índice do elemento recebido\n2- Exibe list\t\t\t\t\t\t\t\t\t5- Quantas vezes elemento aparece na list\n3- Indica a quantidade de elementos na list\t\t\t\t\t6- Indica a quantidade de números inteiros na list\n\t\t\t\t\t\t\t0- Sair''')
    opc = int(input("Digite uma das opções: "))

    while opc < 0 or opc > 6:
        opc = int(input("Tente novamente! Digite uma das opções válidas: "))
    match opc:
        case 0:
            print("Obrigada por utilizar o programa!")
            break
        case 1:
            os.system("cls")
            def preenche_lista(l: list) -> None:
                print("\nAdicione elementos em uma lista, pressione a tecla . para encerrar o programa")
                while True:
                    elemento = input("Elemento: ")
                    if elemento == '.':
                        break
                    else:
                        l.append(elemento)
                print(f"\nResultado da lista: Lista = {l}")

            lista = []
            preenche_lista(lista)
            ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

        case 2:
            os.system("cls")

            def exibe_lista(l: list) -> None:
                print(f"\nLista = {l}")

            lista = [2, 4, 6 ,7]
            exibe_lista(lista)
            ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

        case 3:
            os.system("cls")

            def conta_elementos(l: list) -> int:
                cont = 0
                for i in l:
                    cont +=1
                return cont

            lista = [1,2,3,4,5,6]
            x = conta_elementos(lista)
            print(f"O número de elementos na lista {lista} é igual a {x}")
            ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

        case 4:
            os.system("cls")
            def retorna_indice(elem: int) -> int:
                cont = 0
                for i in lista:
                    cont += 1

                for j in range(cont):
                    if lista[j] == elem:
                        return j
                else:
                    return -1


            lista = [7, 89, 4, 29, 10]
            elemento = int(input("Insira um elemento: "))

            x = retorna_indice(elemento)
            if x == -1:
                print(f"\nValor {elemento} não encontrado na lista\nRetorno: {x}")
            else:
                print(f"\nValor encontrado, o índice do elemento {elemento} é {x}")
            ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

        case 5:
            os.system("cls")

            def busca(l: list, elem: int) -> int:
                cont = 0
                cont2 = 0
                for i in l:
                    cont += 1

                for j in range(cont):
                    if l[j] == elem:
                        cont2 += 1
                else:
                    if cont2 == 0:
                        return -1
                    else:
                        return cont2

            lista = [22, 22, 57, 3, 3, 3]
            elemento = int(input("Digite o elemento inteiro: "))

            x = busca(lista, elemento)

            if x == -1:
                print(f"\nValor {elemento} não encontrado na lista\nRetorno: {x}")
            else:
                print(f"\nO número de vezes que o elemento {elemento} aparece na lista é {x}")
            ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))

        case 6:
            os.system("cls")

            def conta_inteiro(l: list) -> int:
                cont = 0
                cont2 = 0

                for i in l:
                    cont += 1

                for j in range(cont):
                    if type(l[j]) == int:
                        cont2 += 1

                return cont2

            lista = [4, 8, "DS", True, 78, 'P', 45.5]
            x = conta_inteiro(lista)

            print(f"\nO número de elementos inteiros na lista {lista} é {x}")
            ent = int(input("\nDigite uma das opção -> [1]Menu ou [0]Sair\nOpção: "))
else:
    os.system("cls")
    print("Obrigada por utilizar o programa!")