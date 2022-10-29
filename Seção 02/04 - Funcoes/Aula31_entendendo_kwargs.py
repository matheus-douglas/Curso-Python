# Entendendo o **kwargs

"""
- Poderiamos chamar este parâmetro de **qualquercoisa, mas por convenção
chamamos de **kwargs;

-> Este é só mais um parâmetro, mas diferente do *args que coloca os valores
extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e
transforma esses parâmetros em um dicionário.

-> Nas nossas funções, podemos ter (NESTA ORDEM):

- (1) Parâmetros obrigatórios
- (2) *args
- (3) Parâmetros Default (não obrigatórios);
- (4) **kwargs

"""

# Exemplo[1]:

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(matheus='azul', douglas='verde', menezes='branco')

# Obs: Os parâmetros *args e **kwargs não são obrigatórios.

# Exemplo[2]: Mais complexo

def cumprimento_especial(**kwargs):
    if 'Doug' in kwargs and kwargs['Doug'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Doug!'
    elif 'Doug' in kwargs:
        return f'Você recebeu um cumprimento de {kwargs["Doug"]}, Doug!'
    return 'Você não recebeu nenhum cumprimento, pôs não o conheço'

cumprimento_especial()
cumprimento_especial(Doug='Math')
cumprimento_especial(Doug='Python')

# Exemplo[3]: Ordem dos parâmetros

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    return

minha_funcao(25, 'Matheus')  # Somente os parâmetros obrigatórios
minha_funcao(25, 'Doug', 1, 2, 3, solteiro=True)  # Parâmetros obrigatórios, args e Default
minha_funcao(25, 'Menezes', eu='não', voce='Sim')  # Parâmetros obrigatórios, kwargs
minha_funcao(25, 'Fabrício', 9, 4, 5, 2, Java=False, Python=True)  # Parâmetros obrigatórios, args, kwargs
minha_funcao(25, 'Fabrício', 9, 4, 5, 2, solteiro=True, Java=False, Python=True)  # Todos os parâmetros

# {1} Entenda por quê é importante manter a ordem dos parâmetros na declaração

    # Função com a ordem correta de parâmetros:

def mostra_info(a, b, *args, instrutor='Doug', **kwargs):
    return [a, b, args, instrutor, kwargs]

    # Função com a ordem errada de parâmetros

def mostra_info(a, b, instrutor='Doug', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

# {2} Desempacotar com **kwargs: Desempacotando o dicionário com **

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Matheus', 'sobrenome': 'Douglas'}

mostra_nomes(**nomes)

# Obs: Os nomes das chaves do dicionário DEVEM ser os mesmos nomes dos parâmetros da função.
