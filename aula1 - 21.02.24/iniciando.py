# -- comentário de uma linha
"""
Comentário de mais de uma linha
"""

'''
ou assim
'''

# print é o comando de saída de dados (printf)
print("executando via vscode")

# Variáveis
x = 5
print(x, type(x)) # type mostra o tipo da variável
x = 9.8 
print(x, type(x))
x = "Almoço"
print(x, type(x))
x = True # tem que começar com letra maiúscula
print(x, type(x))
x = 5 + 6
print(x)
x = "5" + "6"
print(x)

# Tipos de dados em Python
"""
int - inteiro
float - real
str -  string (texto)
bool - booleano (lógico)
"""

# Casting - mudança de tipo de variável

x = "5"
y = "6"
z = float(x) + float(y) # float() converte a var para float
print(z)
z = int(x) + float(y) # int() converte a var para int
print(z)

rm = str(1234) # str() converte a var para str (string)
print(rm)

# input - entrada de dados (scanf)
valor1 = input("Digite um valor:")
valor1 = float(valor1)
valor2 = input("Digite outro valor:")
valor2 = float(valor2)
resposta = valor1 + valor2
print(resposta)

# ou

valor1 = float(input("Digite um valor:"))
valor2 = float(input("Digite outro valor:"))
resp = valor1 + valor2
print(resp)

# O input sempre lê dados como texto