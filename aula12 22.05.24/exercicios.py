"""
1. Fazer um procedimento que passe uma string por parâmetro e 
transofrme todas as vogais em maiusculo
nome = "Edson de Oliveira"
nome_new = "EdsOn dE OlIvEIrA"

2. Faca uma função que passe uma lista por parâmetro e retorne True caso todos 
sejam inteiros, senao false
lista = [4, 6, 7, 8, 9] True
lista = [5, 3, 5, "Edson"] False
lista = [4, 6, -9, 5] False

3. Sabemos que o metodo isdigit() ou isnumeric() tem uma falha quando 
passamos o sinal de negativo ou positivo
antes do numero contido na string:
print(x.isnumeric("-234"))  <==  Retorna False, deveria ser True.
Faça uma função que pegue uma string por parâmetro e retorne True caso seja um numero 
e True se o numero iniciar
com + ou -.
print(isinteiro("-234")) <== Retorna True
OBS: não utilizar isnumeric() para compor esta nova função
"""