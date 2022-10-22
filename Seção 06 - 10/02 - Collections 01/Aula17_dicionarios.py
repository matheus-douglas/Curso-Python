# Dicionários:

"""
Obs: Em algumas linguagens de programação, os dicionários python são conhecidos
como mapas.

Dicionários são coleçoes do tipo chave/valor.

Exemplo:
[0, 1, 2] -> chave/key
[1, 2, 3] -> valor/velue

# [1] Dicionários são representados por chaves {};

# [2] A separação entre chave/key e valor/value é feita sempre entre (:),
    Onde chave/key vem primeiro -> {'key': 'value'};

# [3] Tanto chave/key quanto valor/value, podem ser de qualquer tipo de dados;

# [4] Podemos misturar os tipos de dados;
"""
print(type({}))

# [1] Criando Dicionários:--------------------------------------------------------------------------

# Forma 1: (Mais comum)

paises1 = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}
print(paises1)
print(type(paises1))

# Forma 2: (Menos comum)

paises2 = dict(br='brasil', eua='Estados unidos', py='Paraguai' )
print(paises2)
print(type(paises2))

# [2] Acessando elementos:--------------------------------------------------------------------------

# Forma (1): Acessando via chave, da mesma forma de lista/tupla
# Obs: Caso tentemos fazer acesso utlilizando uma chave que não exista, teremos o KeyError

print(paises1['br'])
print(paises1['eua'])
print(paises2['br'])


# Forma (2): Acessando via get: Recomendada.
# Obs: Desta forma caso tentemos fazer aceso utilizando uma chave que não exita, retornará (None)

print(paises1.get('br'))
print(paises2.get('eua'))
print(paises2.get('ru'))  # Retorna None

# [3] Forma de verificar o None:--------------------------------------------------------------------

# Forma (1): com if/else

pais = paises1.get('ru')

if pais:
    print(f'País encontrado {pais}')
else:
    print('País não encontrado')

# Forma (2): Passando um parâmetro para substituir o None:

pais = paises2.get('ru', 'Não encontrado')  # O segundo parâmetro passado, substitui o None
print(pais)

# [4] Verificar se a key está contido no dicionário:---------------------------------------------

print('br' in paises1)
print('py' in paises1)
print('ru' in paises1)
print('Brasil' in paises1)  # A busca é feita apenas pela chave/key e não pelo valor/value

# [5] Podemos utilizar qualquer tipo de dado (int, flot, str, bool) inclusive (list, tuple, dict),
# como chaves de um dicionário

# Tuplas por exemplo: São interessantes de serem utilizadas como chaves de dict, por serem imutáveis

localidades = {
    (35.685, 39.6917): 'Escritório em tókio',
    (40.745, 74.7715): 'Escritório em Nova York',
    (55.855, 99.1593): 'Escritório em São Paulo'
}
print(localidades)
print(type(localidades))

# [6] Adicionar elementos em um dicionário:---------------------------------------------------------

# Forma (1): Mais Comum

receita = {'jan': 100, 'fev': 120, 'mar': 160}
print(receita)
print(type(receita))

receita['abr'] = 300  # Adicionei a chave/key 'abr' com o valor/value 300 ao dicionário
print(receita)

# Forma (2): Mais fácil de adicionar mais chaves:valores de uma vez

novo_dado = {'mai': 320, 'jun': 360}  # Gerei uma nova chave/key e um novo valor/value
receita.update(novo_dado)  # Adicionei ao dicionário
print(receita)

# [7] Atualizar dados em um dicionário:-------------------------------------------------------------
# Obs 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário, é a mesma.
# Obs 2: Em dicionários, NÂO podemos ter chaves repetidas.

# Forma (1):

receita['jun'] = 400
print(receita)

# Forma (2):

receita.update({'jun': 450})
print(receita)

# [8] Como remover dados de um dicionário:----------------------------------------------------------

# Forma (1): Mais comum

    # Obs 1: Precisamos SEMPRE informar a chave/key, e caso não seja encontrado, teremos um KeyError

exemplo1 = {'jan': 100, 'fev': 120, 'mar': 160}

exemplo1.pop('jan')
print(exemplo1)

    # Obs 2: Ao removermos um objeto, o valor deste objeto é sempre retornado

exemplo2 = {'jan': 100, 'fev': 120, 'mar': 160}

ret = exemplo2.pop('jan')
print(ret)
print(exemplo2)

# Forma (2):

    # Obs 1: Se a chave/key não existir, será gerado um KeyError
    # Obs 2: Neste caso o valor removido, não é retornado.

exemplo3 = {'jan': 100, 'fev': 120, 'mar': 160}

del exemplo3['fev']
print(exemplo3)

# [9] Alguns métodos de dicionários:----------------------------------------------------------------

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

    # (1) Limpar dicionário: .clear()

d.clear()
print(d)

    # (2) Copiando um dicionário para outro: .copy()

        # 1 ---------------------------------------
novo = d.copy()  # Deep Copy
print(novo)

novo['d'] = 4
print(novo)

print(d)
print(novo)

        # 2 ---------------------------------------

novo = d  # Shalow Copy

print(novo)
novo['e'] = 5

print(d)
print(novo)

    # (3) Forma não usual de criação de dicionário: .fromkeys()

        # Exemplo 1: Gera uma chave e atribui um valor;
outro ={}.fromkeys('a', '3')
print(outro)
print(type(outro))

        # Exemplo 2: Gera uma lista de chaves/key com um mesmo valor atribuido a todas elas;
usuario = {}.fromkeys(['nome', 'senha', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

    # Obs: O método fromkeys recebe dois parâmetros: um iterável e um valor;
    # Ele vair gerar para cada valor do iterável uma chave e irá atribuir a chave o valor informado

        # Exemplo 3: Gera uma chave com cada str e atribui o mesmo valor a todas chaves:
veja = {}.fromkeys('teste', 'valor')
print(veja)

        # Exemplo 4: Cria um range e atribui um valor a cada chave/key do range:
ran = {}.fromkeys(range(1, 11), 'novo')
print(ran)
