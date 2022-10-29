#  Módulo colletions - Ordered Dict

# - Em um dicionário, a ordem de inserção dos elementos não é garantida.

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key, values in dicionario.items():
    print(f'Chaves = {key}: Valor = {values}')

# Realizando o import:

from collections import OrderedDict  # As importações devem ser feitas no topo

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for key, values in dicionario.items():
    print(f'Chave = {key} : Valor = {values}')

# Entendendo a diferença entre Dict e OrderedDict

    # Dicionários comuns:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> Já que a ordem dos elementos não importa para o dicionário

    # Ordered Dict:

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Já que a ordem dos elementos importa para o OrderedDict
