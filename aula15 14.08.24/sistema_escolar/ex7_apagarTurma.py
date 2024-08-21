def apagar_turma(d: dict) -> dict:
    if len(d) > 0:
        d.clear()
        print("\n=========================")
        print("Turma apagada com sucesso!")
        print("=========================")
        return d
    else:
        print("\n=====================")
        print("Turma não possui alunos")
        print("=====================")