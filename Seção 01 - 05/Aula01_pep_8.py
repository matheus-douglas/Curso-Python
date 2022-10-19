"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this
A ideia do PEP8 é que possamos ecrever códigoas Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

----------------------------
Class Calculadora:
    Pass

Classs CalculadoraCientifica:
    Pass
----------------------------

[2] - Utilize nomes em minúsculos, separados por underline para funções ou variáveis;

----------------------------
def soma():
    Pass

def soma_dois():
    Pass

numero = 4

numero_impar = 5
----------------------------

[3] - Utilize 4 espaços para identação! (Não utilizar o Tab)

---------------------------
if 'a' in 'banana':
    print('tem')
---------------------------

[4] - Linhas em branco

---------------------------
- Separa funções e definições de classes com duas linhas em branco;
- Métodos dentro de classe devem ser separados com uma única linha em branco.
---------------------------

[5] - Imports

---------------------------
- Imports devem ser feitos em linhas separadas;

# Import Errado:

import sys, os

# Import Certo:

Import sys
Import os

# Não há problemas em utilizar:

From types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType
    ListType
    SetType
    OutroType
    )

- Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
e antes de constantes ou variáveis globais.
--------------------------------

[6] - Espaços em expressões e instruções:

-------------------------------

# ----Não faça:----

funcao( algo[ 1 ], { outro: 2 } )

algo (1)

dict [ 'chave' ] = lista [indice]

x              = 1
x              = 3
variavel_longa = 5

# ----Faça:----

funcao(algo[1], {outro: 2})

algo(1)

dict['chave'] = lista[indice]

x = 1
x = 3
variavel_longa = 5

------------------------------
[7] - Termine sempre uma instrução com uma nova linha:

"""
