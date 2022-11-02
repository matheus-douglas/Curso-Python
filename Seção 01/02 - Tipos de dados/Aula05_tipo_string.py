# Tipo String:
"""
[1] # Em python um dado é considerado do tipo string sempre que estiver entre aspas simples,
por exemplo:

-> 'uma string' , '123' , 'a' , 'True' , '4.45'

[2] # Em python um dado é considerado do tipo string sempre que estiver entre aspas duplas,
por exemplo:

-> "uma string" , "123" , "a" , "True" , "4.45"

[3] # Em python um dado é considerado do tipo string sempre que estiver entre aspas simples triplas,
por exemplo:

-> '''uma string''' , '''123''' , '''a''' , '''True''' , '''4.45'''

[4] # Em python um dado é considerado do tipo string sempre que estiver entre aspas duplas triplas,
por exemplo:
"""
# -> """uma string""" , """123""" , """a""" , """True""" , """4.45"""


# Exemplo1:
# nome = 'Doug'
# print(nome)
# print(type(nome))

# Exemplo2:
# nome1 = "Doug"
# print(nome1)
# print(type(nome1))

# Exemplo3:
# nome2 = '''Doug'''
# print(nome2)
# print(type(nome2))

# Exemplo4:
# nome3 = 'Matheus \nDouglas'
# print(nome3)
# OBS: em python o \n serve para pular uma linha.

# nome = 'matheus douglas'
# Concatenação -> nome + 'fabricio de menezes' = 'matheus douglas fabricio de menezes'
# multiplicação de string -> nome * 10

# print(nome.upper()) -> .upper() Converte toda a string em maiúsculo
# print(nome.lower()) -> .lower() Converte toda a string em minúsculo
# print(nome.title()) -> .title() Converte a string, tornando apenas a primeira letra em maiúsculo
# print(nome.split()) -> .split() converte toda a string em uma lista
# print(nome[0:16]) -> Slice de string
# print(nome[0:7]) -> Slice de String
# print(nome[::-1]) -> [::-1] Comece do primeiro elemento, vá até o ultimo e inverta a ordem
# print(nome.replace('d', 'T')) -> Substitui o caracter por outro denro da string
# print(f'{(valor que for passado):,.nf}') -> onde n é o número de casas decimais que seram retornados