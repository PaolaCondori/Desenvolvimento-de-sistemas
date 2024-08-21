import os
os.system("cls")

from ex1_cadas import cadastro
from ex2_editar import editar
from ex3_exibir import exibe_alunos
from ex4_excluir import excluir_aluno
from ex5_media import media_turma
from ex6_consulta import consulta_aluno
from ex7_apagarTurma import apagar_turma

notas = {}
opc = 1
while opc == 1:
    
    print("\t0 - SAIR\n\t1 - Adicionar novo Aluno | Nota (limite 10 alunos)\n\t2 - Editar Aluno | Nota\n\t3 - Listar os Alunos\n\t4 - Excluir um Aluno")
    print("\t5 - Calcular a média da turma\n\t6 - Consultar um aluno\n\t7 - Apagar todos os alunos da sala")
    op = input("\nEscolha: ")
    os.system("cls")
    match op:
        case '0':
            print("Obrigada por utilizar o programa!")
            break
        case '1':
            os.system("cls")
            cadastro(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case '2':
            os.system("cls")
            editar(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case '3':
            os.system("cls")
            exibe_alunos(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case '4':
            os.system("cls")
            excluir_aluno(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case '5':
            os.system("cls")
            media_turma(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case '6':
            os.system("cls")
            consulta_aluno(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case '7':
            os.system("cls")
            apagar_turma(notas)
            opc = int(input("\nVoltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
        case _:
            os.system("cls")
            print("Digite uma opção válida !")
            opc = int(input("Voltar ao menu [1] ou Sair do programa [0]\nDigite: "))
            os.system("cls")
else:
    print("\nObrigada por utilizar o programa!")
