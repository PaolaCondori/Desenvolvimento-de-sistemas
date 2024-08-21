import os
import ex12
import ex13

os.system("cls")
def ordena_vetor() -> None:
    f = input("\nVocê deseja ordenar o vetor em crescente [c] ou decrescente [d]?\nResposta: ")
    if f == "c" or f == "C":
        ex12.ordena_vetor_crescente()
    elif f == "d" or f == "D":
        ex13.ordena_vetor_decrescente()

ordena_vetor()