# Estruturas lógicas: and (e), or (ou), not (não), is (é)

"""
Operadores unários:
    -> not
Operadores binários:
    -> and, or, is

Para o 'and', ambos os valores precisam ser True
Para o 'or', um dos valores precisam ser True
Para o 'not' o valor do booleano é invertido, ou seja, se for True se torna False e virse versa.
Para o 'is' o valor é comparado com outro valor, ou seja, usado para comparação

# Tabela verdade: (and)
(True and True)    -> True
(True and False)   -> False
(False and True)   -> False
(False and False)  -> False

# Tabela verdade: (or)
(True or True)    -> True
(True or False)   -> True
(False or True)   -> True
(False or False)  -> False

"""

ATIVO = True
LOGADO = False

# Exemplo (and)
if ATIVO and LOGADO:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Exemplo (not)
if not ATIVO:
    print('Você precisa ativar sua conta, cheque seu e-mail')
else:
    print('Seja bem-vindo usuário')

# Exemplo (or)
if ATIVO or LOGADO:
    print('Você entrou!')

# Exemplo (is)
if ATIVO is True:
    print('Sua conta está ativa')
 