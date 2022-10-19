# listas (List)

"""
Listas em python funcionam como vetores/matrizes (arrays) em outras linguagems,
com a diferença de serem DINÂMICAS e também de podermos colocar QUALQUER tipo de dado.

Linguagens  C/Java: Arrays
    - Possiem tamanho e tipo de dados fixo;
    ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este
    array será sempre do tipo inteiro e poderá ter apenas no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo, ou seja podemos criar a lista e simplismente
  ir adicionando elementos;
- Qualquer tipo de dados: Não possuem tipo de dado fixo, ou seja, podemos colocar
  qualquer tipo de dados

As listas em python são representadas por colchetes: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['D', 'o', 'u', 'g', 'l', 'a', 's']

lista3 = list(range(11))

lista4 = list('Douglas')

lista5 = []

lista6 = ['Programação', 'em', 'python']


# [1] Podemos facilmente checar se determinado valor está contido na lista

# Exemplo com int:
NUM = 11
if NUM in lista3:
    print(f'Encontrei o número {NUM}')
else:
    print(f'Não encontrei o número {NUM}')

# Exemplo com str
if 'u' in lista2:
    print('encontrei a letra procurada ')
else:
    print('Não encontrei a letra procurada ')

# [2] Podemos facilmente ordenar uma lista com o comando: .sort()

lista1.sort()
print(lista1)

# [3] Podemos facilmente contar o numeros de ocorrências de um valor
# em uma lista com o comando: .count()

print(lista4.count('o'))
print(lista1.count(1))

# [4] Podemos facilmente adicionar elementos em listas com o comando: .append()
# Obs: Com o .append() nós só conseguimos adicionar um elemento por vez.

lista1.append(1, 3, 55) # -> = ERRO: Pôs não podemos passar mais de um elemento
print(lista1)

lista1.append([1, 3, 55]) # -> = Permitido: Pôs a lista [] só conta como um elemento
print(lista1)

lista1.append(55)
print(lista1)


# [5] Podemos adicionar ELEMENTOS individualmente a uma lista com o comando: .extend()
# Obs: o comando: .append() adiciona uma lista dentro de outra lista (sublista);
# Já o .extend() adiciona elementos a lista inicial.

lista1.extend([1, 33, 44])
print(lista1)

lista4.extend(' Menezes')
print(lista4)

# [6] Podemos inserir um um novo elemento na lista informando a posição,
# do índice, com o comando: .insert()
# Isso não substitui o valor que ocupa a posição escolhida. o mesmo será deslocado para a direita

lista1.insert(2, 'novo valor')
print(lista1)

# [7] Podemos facilmente juntar duas listas: similar ao .extend()
# Obs: Não é necessario a criação de uma nova variável.

lista6 = lista1 + lista3
print(lista6)

# [8] Podemos facilmente inverter a ordem de uma lista, com o comando: .reverse()
# Similar ao slice de string: [::-1]

lista4.reverse()
print(lista4)

# [9] Podemos facilmente copiar uma lista, com o comando: .copy()

lista6 = lista2.copy()
print(lista6)

# [10] Podemos facilmente saber o numeros de elementos de uma lista, com o comando: .len()

print(len(lista4))

# [11] Podemos remover facilmente o ultimo elemento de uma lista, com o comando: .pop()
# Obs: O .pop() não apenas remove o ultimo elemento da lista, como também o retorna.

lista4.pop()
print(lista4)

# [12] Podemos utilizar o .pop() também para remover o elemento pelo índice: especificando .pop(n)
# Obs: Os elementos a direita desse índice serão deslocados para a esquerda.
# Obs: Se não houver elemento no índice informado, teremos um -> IndexError.

lista4.pop(3)
print(lista4)

# [13] Podemos remover todos os elementos de uma lista. (zerar) com o comando: .clear()

lista2.clear()
print(lista2)

# [14] Podemos também repetir elementos de uma lista dentro dela, com a multiplicação (*)

NOVA = [1, 2, 3]
NOVA = NOVA * 3
print(NOVA)

# [15] Podemos facilmente converter uma string em uma lista, com o comando: .split()
# Obs: Por padrão o .split() separa os elementos da lista pelo espaço entre elas.

CURSO = 'Programação em python'
print(CURSO)
CURSO = CURSO.split()
print(CURSO)

# Também é possivel passar para o .split() o parâmetro pelo qual ele irar separar os elementos;
# Exemplo: .split(',') dessa forma os elementos seram separados pela vírgula, e não pelo espaço.

# [16] Podemos converter uma lista em uma string, com o comando: .join()
# Obs: oque vem entre aspas antes do .join() define oque vai ficar entre um elemento e outro;

# Nesse caso foi o ' ' Espaço em branco:
CURSO = ' '.join(lista6)
print(CURSO)
# Nesse caso foi o '$' cifrão:
CURSO = '$'.join(lista6)
print(CURSO)
# Nesse caso foi o '-' traço:
CURSO = '-'.join(lista6)
print(CURSO)

# [17] Iterando sobre listas:

# Exemplo1 -> utilizando o for:
SOMA = 0
for elemento in lista1:
    print(elemento)
    SOMA = SOMA + elemento
print(SOMA)

# Exemplo2 -> utilizando while:

carrinho = []
PRODUTO = ''

while PRODUTO != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    PRODUTO = input()
    if PRODUTO != 'sair':
        carrinho.append(PRODUTO)

for PRODUTO in carrinho:
    print(PRODUTO)

# [18] Podemos utilizar variáveis em listas:

numeros = [1, 2, 3, 4, 5]
print(numeros)

NUM1 = 1
NUM2 = 2
NUM3 = 3
NUM4 = 4
NUM5 = 5

numeros = [NUM1, NUM2, NUM3, NUM4, NUM5]
print(numeros)

# [19] Fazemos acesso aos elementos de forma indexada

#       [    0         1        2        3    ]
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

for cor in cores:
    print(cor)

INDICE = 0
while INDICE < len(cores):
    print(cores[INDICE])
    INDICE = INDICE + 1

# [20] Podemos gerar indice em um for:

cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)

# [21] -> Encontrar o índice de um elemento na lista com o comando: .index()

numeros = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
print(numeros.index(7))
print(numeros.index(4))

# Obs: Caso não tenha este elemento na lista, será apresentado erro valueError
# Obs: Em casos de elementos em duplicidade, será retornado o index do primerio valor encontrado

# [22] Podemos fazer buscas dentro de um range, ou seja, qual index começar a buscar:

print(numeros.index(5, 1)) # Buscando a partir no index (1)
print(numeros.index(5, 2)) # Buscando a partir no index (2)
print(numeros.index(5, 3)) # Buscando a partir no index (3)

# [23] Trabalhando com slice de lista com parâmetro 'inicio':

lista = [1, 2, 3, 4, 5]
print(lista[1:]) # Iniciando do index 1 e pegando os demais elementos.
print(lista[::]) # Abrange todos os elementos da lista.

# [24] Trabalhando com slice de lista com parâmetro 'fim':

lista = [1, 2, 3, 4, 5]
print(lista[:2]) # Começa em 0, e pega até o index (2) -1
print(lista[:4]) # Começa em 0, e pega até o index (4) -1

# [25] Trabalhando com slice de lista com parâmetros 'inicio e fim':

lista = [1, 2, 3, 4, 5]
print(lista[1:3]) # Começa em 1, e pega até o index (3) -1

# [26] Trabalhando com slice de lista com parâmetro 'passo'

lista = [1, 2, 3, 4, 5]
print(lista[1::2]) # Começa em 1, e vai até o final, de (2) em (2)
print(lista[::2])  # Começa em 0, e vai até o final, de (2) em (2)

# [27] Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(lista))  # SOMA: sun() / Só para listas de valors inteiros e/ou reias
print(max(lista))  # Máximo: max() / Só para listas de valors inteiros e/ou reias
print(min(lista))  # Mínimo: min() / Só para listas de valors inteiros e/ou reias
print(len(lista))  # Tamanho: len()

# [28] Transformação de uma lista em uma tupla:

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = tuple(lista)
print(tupla)
print(type(tupla))  # Verificação

# [29] Desempacotamento de listas:

lista = [1, 2, 3]

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# Obs: O número de elementos a serem desempacotados devem ser iguais ao numeros de variáveis,
# caso contrário teremos ValueError

# [30] Copiando uma lista para outra (Shallow copy e Deep copy)

# Deep Copy:

lista = [1, 2, 3, 4]
print(lista)
nova = lista.copy()  # Cópia que preserva a original
nova.append(5)
print(nova)
print(lista)
# Obs: Note que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a original

# Shallow Copy:

lista = [1, 2, 3, 4]
print(lista)
nova = lista  # Cópia que não preserva a original
nova.append(5)
print(nova)
print(lista)
