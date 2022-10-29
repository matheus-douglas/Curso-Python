# Funções com retorno
"""
numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'Retorno do .pop() : {ret_pop}')

ret_pr = print(numeros)  # A função print() não retorna nada!
print(f'Retorno do print() : {ret_pr}')

----------------------------------------------------------------------------------------------------

# Exemplo de função:

def quadrado_de_7():
    print(7 * 7)
#OBS: Nossa função está executando outra função que é a print(), logo, ela não retorna nada

ret = quadrado_de_7
print(f'Nossa função retorna {ret}')  # None
----------------------------------------------------------------------------------------------------

[1]* - Em Python, quando uma função não retorna valor, o retorno é None;

[2]* - Funções Python que retornam, devem retornar estes valores com a palavra reservada return

[3]* - Não precisamos necessariamente criar uma variável para receber o retorno de uma função;
Podemos passar a execução da função para outras funçõs.

[4] - Palavra reservada return:
    (1) - Ela finaliza a função, ou seja, ela sai da execução da função;
    (2) - Podemos ter em uma função, diferentes returns;
    (3) - Podemos em uma função, retornar qualquer tipo de dados e múltiplos valores

----------------------------------------------------------------------------------------------------

"""
# Agora iremos refatorar esta função para que ela retorne o valor:

def quadrado_de_7():
    return 7 * 7

RET = quadrado_de_7()  # Criamos ussa variável para receber o return da função
print(f'O retorno é {RET}')

print(f'O retorno é {quadrado_de_7()}')  # Aqui tivemos o retorno direto sem criar variável

# Refatorando a primeira função que criamos na aula passada: 

def diz_oi():
    return 'oi'

print(diz_oi())

# Exemplos sobre o return:

    # Exemplo *[1]:
def diz_oi():
    print('Estou sendo executado antes do return...')
    return 'oi'
    print('Estou sendo executado após o return...')  # Nunca será executada, pôs está após o return

print(diz_oi())

    # Exemplo *[2]:
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

    # Exemplo *[3]:
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()  # Desempacotando
print(num1, num2, num3, num4)  # Imprimindo os valores desempacotados

print(outra_funcao())  # Imprimindo direto -> Gera uma tupla

# [Vamos criar uma função para jogar a moeda: Game 'Cara ou Cora']

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'

joga_moeda()