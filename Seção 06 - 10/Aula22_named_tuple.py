# Módulo Collections - Named Tuple

"""
- Recapitulando Tuplas:

tulpe = (1, 2, 3, 4)
print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também
parâmetros.

"""
# Realizamos o import:

from collections import namedtuple

# Prectupleisamos definir o nome e parâmetros.

    # Forma (!): Declaração Named Tuple
CACHORRO = namedtuple('cachorro', 'idade raca nome')

    # Forma (2): Declaração Named Tuple
CACHORRO = namedtuple('cachorro', 'idade, raca, nome')

    # Forma (3): Declaração Named Tuple
CACHORRO = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando:

ray = CACHORRO(idade=2, raca='chow-chow', nome='ray')
print(ray)

# Acessando dados:

    # Forma (1): - Pelo index
print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

    # Forma (2): - Pela key
print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  #nome
