def excluir_aluno(d: dict) -> dict:
    print("=============")
    print("Excluir Aluno")
    print("=============\n")
    aluno = input("Nome: ")
    if d.get(aluno):
        del d[aluno]
        print("\n===================")
        print("Aluno excluído com sucesso!")
        print("===================")
    else:
        print("\n===================")
        print("O aluno não existe")
        print("===================")

    return d