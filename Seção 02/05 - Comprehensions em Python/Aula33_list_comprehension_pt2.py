# List Comprehension

"""
- Nós podemos adicionar estruturas condicionais lógicas ás nossas list comprehension

"""

# Exemplo [1]:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(pares)
print(impares)

# Refatorando (1):

# Qualquer número par (módulo de 2) o resto é igual a 0, e 0 em Python é False. Not false = True
par = [num for num in numeros if not num % 2]

# Qualquer número impar (módulo de 2) o resto é igual a 1, e 1 em Python é True
impar = [num for num in numeros if num % 2]

print(par)
print(impar)

# Exemplo [2]:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(res)
