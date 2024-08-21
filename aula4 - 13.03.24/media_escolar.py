import os
os.system("cls")

notasSala = []
cont = 0
for i in range(1,11):
    print("Notas do aluno {}".format(i))
    notasAluno = []
    for j in range(1,4):
        #Digitar as 3 notas
        nota = float(input("Digite a nota {}: ".format(j)))

        #Verificar se a nota está entre 0 e 10
        while nota < 0 or nota > 10:
            print("Nota inválida!")
            nota = float(input("Digite a nota {} novamente: ".format(j)))
        notasAluno.append(nota)
        notasAluno.sort()

    #Descartando menor nota
    notasAluno.remove(notasAluno[0])

    #Média entre 2 notas
    mediaAluno = sum(notasAluno)/2
    print("Media do aluno: {}".format(mediaAluno))
    notasSala.append(mediaAluno)
    if mediaAluno >= 9:
        cont += 1
    print("\n")
mediaSala = sum(notasSala)/10

#Exibir média da sala
print("Média da sala: {}".format(mediaSala))

#Quantos tiraram média igual a 9
print("Quantidade de alunos que tiraram médias maior ou igual a 9: {}".format(cont))