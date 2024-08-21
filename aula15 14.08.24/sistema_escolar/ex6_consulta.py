def consulta_aluno(d: dict) -> None:
    print("===============")
    print("Consulta aluno")
    print("===============\n")
    aluno = input("Nome: ")
    for k in d.keys():
        if k == aluno:
            print(f"\nAluno: {k}    Nota: {d[k]}")
            break
    else:
        print("\n===================")
        print("O aluno não existe")
        print("===================")