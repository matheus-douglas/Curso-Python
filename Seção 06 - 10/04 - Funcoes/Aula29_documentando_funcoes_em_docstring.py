# Documentando funções com docstrings

"""
Para documentar sua função você precisa utilizar aspas duplas triplas dentro do bloco da função.

- Pdemos ter acesso a documentação de uma função em Python, utilizando a propiedade especial .__doc__

- Podemos ainda ter acesso a uma documentação de uma função em Python, utilizando a já conhecida função help();

"""

# Exemplo[1]:

def diz_oi():
    """Uma função simples que retorna a string 'oi!'"""
    return 'oi!'

diz_oi()
print(help(diz_oi))
print(diz_oi.__doc__)

# Exemplo[2]:

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado do 'numero',
    Ou 'numero' elevado á 'potencia' informada.
    ------------------------------------------------------------
    :param numero: Número que desejamos saber o exponencial.
    :param potencia: Potência a qual desejamos elevar o 'numero'.
    :return: Retorna o 'numero' elevado á 'potencia'
    """
    return numero ** potencia

exponencial(2, 3)
print(exponencial.__doc__)
print(help(exponencial))
