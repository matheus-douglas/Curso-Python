# Expressões Lambdas

"""
- Utilizando lambdas:

Conhecidas por expressões lambdas, ou simplismente lambdas, são funções sem nome, ou seja,
funções anônimas.

# Recapitulando funções em Python:

def soma(a, b):
    return a + b

# Sintaxe da expressão lambda:

    lambda parâmetro: retorno

"""

# Exemplo [01]: Função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Exemplo [02]: Exepressão lambda

lambda x: 3 * x + 1

# Como utilizar a expressão lambda? nomeando-a

calc = lambda x: 3 * x + 1

print(calc(4))

# {01} Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' matheus ',' douglas  '))

# {02} Em lambdas podemos ter numhuma ou várias entradas: Parâmetros

nenhuma = lambda: 'Não recebe parâmetros'

um = lambda x: x * x + 1

dois = lambda x, y: x + y / 2

tres = lambda x, y, z: 3 * x - y / z

print(nenhuma())
print(um(4))
print(dois(4, 5))
print(tres(4, 5, 6))

# Obs: Se passarmos um número de argumentos diferentes do número de parâmetros definidos, teremos TypeErro

# Exemplo [03]: outros

autores = ['Elizabeth Kostova', 'Edgar Allan Poe', 'Clive Barker', 'Bram Stoker', 'Ant Lima', 
'Anne Rice', 'Ambrose Bierce', 'H. G. Whells', 'Arthur C. Clarke', 'Orson Scott Card']

print(autores)

# Utilizando o .sort() para ordenar a lista autores; passando a expressão lambda como chave pra essa ordenação,
# e a expressão lambda tem como parâmetro o sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Exemplo [04]: Função quadrática

# f(x) = a * x ** 2 + b * x + c

    # Definindo a função:

def funcao_quadrada(a, b ,c):
    """Função que retorna f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

# Variavel  = return Lambda  (a, b,  c)
nome_lambda = funcao_quadrada(2, 3, -4)

#    (lambda     (x))
print(nome_lambda(5))
print(nome_lambda(0))

# Printando direto:

# Informamos os parâmetros da função > ela retorna a lambda > informamos o parâmetro da lambda;

#                    (a, b,  c)(x)
print(funcao_quadrada(2, 3, -4)(5))