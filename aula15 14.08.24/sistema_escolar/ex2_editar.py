        
def editar(d: dict) -> dict:
    print("=============")
    print("Editar aluno")
    print("=============\n")

    aluno = input("Nome: ")

    if d.get(aluno):
        print(f"Nota: {d[aluno]}")
        nota = float(input("Nova Nota: "))
        if nota < 0 or nota > 10:
            print("\n==============")
            print("Nota inválida")
            print("==============")
        else:
            d[aluno] = nota
    else:
        print("\n===================")
        print("O aluno não existe")
        print("===================")

    return d