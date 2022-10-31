# Set comprehension (conjunto)

"""
- Lembrese conjuntos são parecidos com os dicionários, porém não tem as chaves;
os set também não guardam ordenações nem valores repetidos.
"""
# Exemplo [01]:

numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo [02]:

numeros = {num ** 2 for num in range(10)}
print(numeros)

# Exemplo [03]:
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Exemplo [04]: Strings

letras = {letra for letra in 'Matheus Douglas'}
print(letras)

# Obs: Lembrando que em conjuntos (Set), não existe repetição nem ordenação