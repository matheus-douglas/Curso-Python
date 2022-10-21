# Módulo collections - Default Dict

"""
- Recapitulando dicionário:--------------------
dicionario = {'curso': 'Programação em Python'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # Gera KeyError
------------------------------------------------

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma key que não existe, essa chave será criada
e o valor default será atribuído.

Obs: (Lambdas) são (funções) sem nome, que podem ou não receber parâmetros de entrada
e retonar valores.

"""

# Realizando o import:

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'programação em Python'

print(dicionario)
print(dicionario['outro'])  # KeyError acontece no dicionário comum, mas não aqui
print(dicionario)
