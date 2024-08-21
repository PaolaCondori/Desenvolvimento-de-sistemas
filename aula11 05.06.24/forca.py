import os
os.system("cls, clear")

"""Algoritmo para o jogo da forca
1- Definir a palavrasecreta
2- Definir quantidade de chances
3- Criar o input do usuário
4- Verificar se o input é válido
5- Verificar se a letra digitada está na palavra secreta
6- Exibir ao usuário se lee acertou e o atual número de chances
7- Exibir se o usuário ganhou ou não
"""
palavra_secreta = "Vaticano"
qtd_chances = 6
palavra_secreta = palavra_secreta.lower()

while True:
    print("JOGO DA FORCA\n\n")
    for i in range(len(palavra_secreta)):
        print("_", end = " ")
        
    letra = input("\n\nDigite uma letra: ")
    
    if letra in palavra_secreta:
        print("Você")
    break