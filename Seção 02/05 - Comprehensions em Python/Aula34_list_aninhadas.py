# Listas aninhadas (Nested List)

"""
- Algumas linguagens de programação como (C/Java/PhP...) possuem uma estrutura de dados chamadas de Arrays;
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

- Em Python nós temos as listas:

num = [1, 'b', 3.453, True, 5]

"""

# Exemplo [1]:

listas = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]  # Matriz 3x3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1])  # Fazemos acesso aos indices das linhas e colunas. Linha[0], coluna[1] = 2
print(listas[2][1])  # Linha[2], coluna[1] = 8

# Iterando com loops em uma lista aninhada:

for lista in listas:
    print(lista)  # Retorna todas as listas que estavam contidas na variável listas

for lista in listas:
    for num in lista:
        print(num)  # Retorna todos os números que estavam contidos nas listas dentro da variál listas

# Utilizando lis comprehension: Lembrando que a sintaxe é como se fosse lida de trás para frente

[[print(valor) for valor in lista] for lista in listas]

# Exemplo [2]: Gerando um tabuleiro/matriz 3x3

tabuleiro = [[num for num in range(1, 4)] for valor in range(1,4)]
print(tabuleiro)

# Exemplo [3]: Gerando jogadas para o jogo da velha

velha = [['X' if num % 2 == 0 else 'O' for num in range(1, 4)]for valor in range(1, 4)]
print(velha)
