def exibicao_manual(d: dict) -> None:
    print(f"Nome.....:{d['nome']}")
    print(f"Idade.....:{d['idade']}")
    print(f"Casado.....:{d['casado']}")
    print(f"Peso.....:{d['peso']}")

def exibicao_metodos(d: dict) -> None:
    for k, v in d.items():
        print(f"{k} -> {v}")

import os
os.system("cls")

#projeto :o

dicionario = {} # ou dict()
print(dicionario)

contato = {
    # 'Key': value, 
    'nome': 'Edson',
    'idade': 50,
    'casado': True,
    'peso': 80.9,
}
#Exibição bruta
print(contato)

#Exibição manual
print(f"Nome.....:{contato['nome']}")
print(f"Idade.....:{contato['idade']}")
print(f"Casado.....:{contato['casado']}")
print(f"Peso.....:{contato['peso']}")

#adicionando um novo valor ao dicionario
contato['altura'] = 1.70
print(contato)

"""
# Remover uma key
del contato['altura']
print(contato)

contato.pop('nome')
print(contato)

"""
os.system("cls")

#Método keys() pega o nome das chaves do dicionario
"""
# Manipulando as chaves
print(contato.keys())
print(list(contato.keys()))

for chave in contato.keys():
    print(chave)

print(contato.values())
print(list(contato.values()))

for chave in contato.values():
    print(chave)
"""

# manipulando os items
os.system("cls")
print(contato.items())
print(list(contato.items()))
for k, v in contato.items():
    print(f"{k} -> {v}")

os.system("cls")

exibicao_manual(contato)
del contato['nome']
exibicao_metodos(contato)