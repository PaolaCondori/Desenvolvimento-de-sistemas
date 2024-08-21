def media_turma(d: dict) -> None:
    print("===============")
    print("Média da turma")
    print("================\n")
    notas = 0
    for v in d.values():
        notas += v
    print(f"Média da turma: {notas/len(d)}")