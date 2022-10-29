# Conjuntos

"""
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência á teoria dos conjuntos
da matemática.

- aqui em python os conjuntos são chamados de Sets.

Disto isso, da mesma forma que na matemática:
    - Sets (conjuntos) não possuem valors duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

- Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

- Os conjuntos (Sets) são referenciados em python com chaves {}

- Diferenças ente conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chaves/valor;
    - Um conjunto tem apenas valor;

"""

# [1] Definindo um conjunto:

    # Forma 1:

# s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.
# print(s)
# print(type(s))

# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parde do conjunto.

    # Froma 2: - Mais comum

# s = {1, 2, 3, 4, 5, 5}  # Valores repetidos, são ignorados
# print(s)
# print(type(s))

# [2] Podemos verificar se determinado elemento está contido no conjunto:

# if 3 in s:
#    print('Está contido')
# else:
#    print('Não está contido')

# [3] Importante lembrar que, além de não termos valores duplicados, não temos ordem;

DADOS = 99, 2, 34, 23, 12, 2, 34, 1, 44, 5

    # Listas aceitam valores duplicados, então temos 10 elementos;
lista = list(DADOS)
print(f'Lista: {lista} com {len(lista)} elementos')

    # tuplas aceitam valores duplicados, então temos 10 elementos;
tupla = tuple(DADOS)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

    # Dicionários não aceitam chaves duplicados, então temos 8 elementos;
dicionario = {}.fromkeys(DADOS, 'dict')
print(f"Dicionário: {dicionario} com {len(dicionario)} elementos")

    # Sets não aceitam valores duplicados, então temos 8 elementos;
conjunto = set(DADOS)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# [4] Assim como todos outros conjuntos Python podemos colocar tipos de dados misturados em Sets:

s = {1, 'b', False, 34.22, 44}
print(s)
print(type(s))

    # Podemos iterar em um Set normalmente:
for valor in s:
    print(valor)

# [5] Usos interessantes com Sets:

    # Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu;
    # e os visitantes informam manualmente a cidade de onde vieram.

    # Adicionamos cada cidade em uma lista, já que em uma lista podemos adicionar novos elementos.
    # e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

    # Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos?

print(len(set(cidades)))

# [6] Adicionar elementos em um conjunto:

s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera error, simplismente é ignorado e não é adicionado.
print(s)

# [7] Remover elementos em um conjunto:

s = {1, 2, 3}

    # Forma 1:
s.remove(3)  # Não é index, informamos o valor a ser removido
print(s)
# Obs: Caso o valor a ser removido não for encontrado, será gerado o valor KeyError

    # Forma 2:
s.discard(2)
print(s)
# Obs: Caso o valor a ser removido não for encontrado, nenhum erro é gerado

# [8] Copiando um conjunto para outro:

s = {1, 2, 3, 4, 5, 6}
print(s)

    # Forma 1: Deep Copy
novo = s.copy()
print(novo)

novo.add(7)
print(novo)
print(s)

    # Forma 2: Shallow copy
novo = s
print(novo)

novo.add(7)
print(novo)
print(s)

# [9] Podemos remover todos os itens de um conjunto:

s.clear()
print(s)

# [10] Métodos matemáticos de conjuntos:

    # Imagine que temos dois conjuntos: um contendo estudantes do curso Python
    # e um contendo estudantes do curso Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

    # Vejam que algums alunos que estudam python, também estudam java;
    # (1) Precisamos gerar um conjunto com nomes de estudantes únicos:

# Forma 1: Utilizando .union():

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2: Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

    # (2) Precisamos gerar um conjunto com estudantes que estão em ambos os grupos:

# Forma 1: Utilizando o .intersection():

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2: Utilizando o &:

ambos2 = estudantes_python & estudantes_java
print(ambos2)

    # (3) Precisamos gerar um conjunto de estudantes que estão em apenas um dos grupos:

# Forma 1: Utilizando o .difference():

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

    # (4) Soma, valor máximo*, valor mínimo*, tamanho*
        # * se os valores forem todos inteiros ou reais int/float;

s = {1, 2, 3, 4, 5, 6, 7}

print(sum(s))  # Soma;
print(max(s))  # Valor Máximo;
print(min(s))  # Valor Mínimo;
print(len(s))  # Total.
