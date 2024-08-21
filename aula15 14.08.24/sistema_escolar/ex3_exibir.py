def exibe_alunos(d: dict) -> None:
    print("=================")
    print("Exibição da turma")
    print("=================\n")

    largura_nome = 30
    largura_nota = 4
    #Alinhamento do cabeçalho
    print("Aluno".ljust(largura_nome) + "Nota".rjust(largura_nota))
    print("-"  * (largura_nota + largura_nome ))

    #Alinhamento da key e do value
    for k, v in sorted(d.items()):
       print(k.ljust(largura_nome) + str(v).rjust(largura_nota))
