def cadastro(d: dict) -> dict:
    print("======================")
    print("Cadastre um novo aluno")
    print("======================\n")

    aluno = input("Nome: ")
    nota = input("Nota: ")
    
    if not nota.replace(".", "").isnumeric():
            print(nota)
            print("\n==============")
            print("Nota inválida")
            print("==============")
    elif (float(nota) < 0 or float(nota) > 10):
            print("\n==============")
            print("Nota inválida")
            print("==============")
    else:
        if d.get(aluno):
            print("\n==================")
            print("O aluno já existe")
            print("==================")
        else:
            d[aluno] = float(nota)
            print("\n==============================")
            print("Aluno cadastrado com sucesso!")
            print("==============================\n")

    return d