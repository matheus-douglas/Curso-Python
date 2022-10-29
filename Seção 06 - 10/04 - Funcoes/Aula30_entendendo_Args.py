# Entendendo o *args

"""
- O *args é um parâmetros como outro qualquer. isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco

Exemplo:

    *qualquercoisa

Mas por convenção, utilizamos o *args para definí-lo

- Mas oque é o *args?

O parâmetros *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""

# Exemplo[1]: Sem utilizar o *args

def soma_todos_os_numeros(num1, num2, num3):
    return num1 + num2 + num3 

soma_todos_os_numeros(1, 3, 5)  # Resultado = 9
soma_todos_os_numeros(1, 3)  # TypeError -> pôs falta um parâmetro
soma_todos_os_numeros(1, 3, 5, 7)  # TypeError -> pôs passamos parâmetros demais

# Exemplo[2]: Refatorando a função utilizando o *args

def soma_todos_os_numeros(*args):
    total = 0
    for num in args:
        total = total + num
    return total

soma_todos_os_numeros()
soma_todos_os_numeros(1, 3, 5)
soma_todos_os_numeros(1, 3)
soma_todos_os_numeros(1, 3, 5, 7)

# Exemplo[4]: Refatorando ainda mais a função anterior

def soma_todos_os_numeros(*args):
    return sum(args)

soma_todos_os_numeros()
soma_todos_os_numeros(1, 3, 5)
soma_todos_os_numeros(1, 3)
soma_todos_os_numeros(1, 3, 5, 7)


# Exemplo[5]: Outras utilizações para o *args

def verifica_info(*args):
    if 'Matheus' in args and 'Menezes' in args:
        return 'Eu conheço Matheus Menezes'
    return 'Eu não tenho esses dados na minha base'

verifica_info()
verifica_info('Matheus')
verifica_info('Matheus', 'Menezes')
verifica_info(1, 'eu', 35.55, True)

# Exemplo[6]: Trabalhando com desempacotamento

def soma(*args):
    return sum(args)

num = [1, 2, 3, 4, 5, 6, 7]  # Variável do tipo List

soma(num)  # TypeError -> pôs a lista não foi desempacotada, logo é considerada apenas 1 elemento
soma(*num)  # O asterisco serve para informar ao Python que estamos passando uma coleção de dados,
# logo o Python entende que precisa desempacotar os valores dessa coleção antes de realizar alguma operação.
