# List Comprehension


# - Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
# iterável.
# -> Sintaxe da List Comprehension
# [dado for dado in iterável]


# Exemplo [1]:

list1 = [1, 2, 3, 4, 5]

res = [num * 10 for num in list1]

print(res)

# Exemplo [2]:

list2 = [1, 2, 3, 4, 5]

res1 = [num ** 2 for num in list2]

print(res1)

"""
- Para entender melhor o que está acontecendo, devemos dividir a expressão em duas partes:

- A Primeria parte: for num in list1
- A Segunda parte: num * 10

Ou seja, toda opeção que nós desejarmos que seja realizada é declarada antes do for. como se 
a expressão fosse lida de trás para frente.
"""

# {1} List Comprehension vs Loop:

    # (Loop)

lista = [1, 2, 3, 4, 5]

lista_dobrada = []

for num in lista:
    lista_dobrada.append(num * 2)

print(lista_dobrada)

    # (List Comprehension)

lista = [1, 2, 3, 4, 5]

res = [num * 2 for num in lista]

print(res)


# Exemplo [3]:

nome = 'matheus douglas'

print([letra.upper() for letra in nome])

# Exemplo [4]:

amigos = ['doug', 'math', 'mnz']

print([amigo.title() for amigo in amigos])

# Exemplo [5]:

print([numero * 3 for numero in range(1, 10)])

# Exemplo [6]:

print([bool(valor) for valor in [0, [], '', True, 1, 3.55]])

# Exemplo [7]:

print([str(num) for num in range(1, 10)])
