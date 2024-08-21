import os 
os.system("cls")


cont = 1
while cont == 1:
    os.system("cls")
    print("MENU")
    print("1 - Tabuada\n2 - Vogais")
    opcao = int(input("Digite uma das opções: "))
    
    match opcao:
        case 0:
            break
        #Exercício 1
        case 1:
            num = int(input("Digite um número: "))

            for i in range(0,10):
                multi = num * (i+1)
                print("{} * {} = {}".format(num, i+1, multi))
            cont = int(input("Digite [1] para voltar ao menu ou [0] para sair: "))

        #Exercício 2
        case 2:
            cont = 0
            for i in range(1,6):
                num = input("Digite caracter {}: ".format(i))
                if num == 'a' or num == 'e' or num == 'i' or num == 'o' or num == 'u':
                    cont += 1
            print("{} vogais".format(cont))
            cont = int(input("Digite [1] para voltar ao menu ou [0] para sair: "))

        case _:
            print("Opção inválida")
            cont = int(input("Digite [1] para voltar ao menu ou [0] para sair: "))
    continue

