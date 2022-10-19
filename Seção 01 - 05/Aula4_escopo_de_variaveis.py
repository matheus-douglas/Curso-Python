"""
Escopo de variáveis

/                              /

[1] -> Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
[2] -> Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarado

Para declarar variáveis em Python, fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. isso significa que
ao declararmos uma variável, nós nçao colocamos o tipo de dado dela.
Estes tipo é inferido ao atribuirmos o valor da mesma.

Exemplo em C:
    int numero = 42
Exemplo em java:
    int numero = 42
Exemplo em python:
    numero = 42
"""

NUMERO = 42
print(NUMERO)
print(type(NUMERO))

# novo = 0 -> novo é uma variável global, difinida fora de um bloco

if NUMERO > 10:
    NOVO = NUMERO + 10  # novo é uma variável local, definida dentro do bloco if
    print(NOVO)
