# Tuplas (tuple)

"""
Tuplas são bastantes parecidas com listas.
Existem duas diferenças básicas:

[1] - As tuplas são representadas por parênteses ()

[2] - As tuplas são imutáveis: isso significa que ao se criar uma tupla ela não muda;
toda operação feita em uma tupla gera uma nova tupla.

[3] - Métodos de adição ou remoção de elementos nas tuplas não existem, já que elas são imutáveis

------------------------------------------------------------------------------------
-> Por quê utilizar tuplas?

- Tuplas são mais rápidas do que listas.
- Tuplas deixam seu código mais seguro*
    - *Isso porque trabalhar com elementos imutáveis traz segurança para o código;

"""
print(type(()))

# CUIDADO [1]: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

# CUIDADO [2]: Tuplas com 1 elemento:

TUPLA3 = (4)  # Isso não é uma tupla!
print(TUPLA3)
print(type(TUPLA3))

tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo parênteses.

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# [1] Gerando uma tupla dinamicamente com range:

tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))

# [2] Desempacotamento de tupla:

tupla7 = ('Matheus douglas', 'fabricio de menezes')

nome, sobrenome = tupla7

print(nome)
print(sobrenome)

# Gera ValueError se o numero de elementos a serem desempacotados for
# diferente do numero de variáveis.

# [3] Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

tupla8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(sum(tupla8))  # SOMA: sun() / Só para listas de valors inteiros e/ou reias
print(max(tupla8))  # Máximo: max() / Só para listas de valors inteiros e/ou reias
print(min(tupla8))  # Mínimo: min() / Só para listas de valors inteiros e/ou reias
print(len(tupla8))  # Tamanho: len()

# [4] Concatenação de tuplas:

tupla9 = (1, 2, 3)
print(tupla9)

tupla10 = (4, 5, 6)
print(tupla10)

print(tupla9 + tupla10) # Concatenação

print(tupla9)  # Note que a concatenação não fere o principio da imutabilidade da tupla
print(tupla10) # Note que a concatenação não fere o principio da imutabilidade da tupla

tupla11 = tupla9 + tupla10  # Tuplas são imutáveis, porém podemos sobescrever seus valores
print(tupla11)

# [5] Verificar se um determinado elemento está contido na tupla:

tupla12 = (1, 2, 3)
print(3 in tupla12)
print(5 in tupla12)

# [6] Iterando sobre uma tupla:

tupla13 = (3, 4, 5)

for n in tupla13:
    print(n)

for indice, valor in enumerate(tupla13):
    print(indice, valor)

# [7] Contando elementos dentro de uma tupla:

tupla14 = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla14.count('a'))

# [8] Convertendo uma string para tupla:

NOME = tuple('Matheus Douglas')
print(NOME)

# DICAS NA UTILIZAÇÃO DE TUPLAS:

# [1] - Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em coleções

    # - Exemplo:

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(meses)

# [2] - O acesso a elementos de uma tupla também é semelhante a de uma lista: Pelo index

print(meses[4])

# [3] - Iterar com o while:

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# [4] - Verificando em qual indice o elemento está na tupla:

print(meses.index('jun')) # Caso o elemento não exista na tupla será gerando o ValueError

# [5] - Slicing: [inicio:fim:passo]:

#   - Exemplos:
print(meses[0:])
print(meses[0::2])
print(meses[::-1])
