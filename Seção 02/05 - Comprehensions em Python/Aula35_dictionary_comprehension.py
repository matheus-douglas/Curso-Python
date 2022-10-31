# Dictionary comprehension

"""
-> Pense no seguinte:

- Se quisermos criar uma lista:

lista = [1, 2, 3, 4, 5]

- Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4, 5) ou 1, 2, 3, 4, 5

- Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4, 5}

- Se quisermos criar um dincionário:

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Syntax do dictionary comprehension:

{chave=valor for valor in iteravel}

"""

# Exemplo [01]: transformando um dict

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Para cada chave e valor na minha variavel numeros, pegue a chave e atribua a ela o
# quadrado do valor e liste o resultado
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# Exemplo [02]: transformando uma lista (Se aplica a tuplas e set's também)

numeros1 = [1, 2, 3, 4]

# Para cada valor na minha variavel numeros1, pegue esse valor e transforme ele na chave 
# e atribua a essa chave, o quadrado desse valor
quadrado1 = {valor: valor ** 2 for valor in numeros1}

print(quadrado1)

# Exemplo [03]: Formando um dicionário

chaves = 'matheus'
valores = [1, 2, 3, 4, 5, 6, 7]

# Para cada index no meu range q vai de 0 á total da variavel chaves, pegue um index dessa
# chave e atribua o valor do index correspondente
dicionario = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(dicionario)

# Exemplo [04]: com lógica condicional

numeros2 = [1, 2, 3, 4, 5, 6, 7]

# Para cada numero na minha variavel numeros2, transforme esse numero em chave e atribua o
# valor 'par' ou 'impar' seguindo a condicional
res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros2}

print(res)
