# Funções com Parâmetro (de entrada)

"""
- Funçoes que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

Entrada -> Porcessamento -> Saída

Se a gente pensar em uma função, já sabemos que temos funções que:
    - Não possuem entrada;
    - Não possuem saída;
    - Possuem entrada mas não possuem saída;
    - Não possuem entrada mas possuem saída;
    - Possuem entrada e saída.

- Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos
parâmetros forem necessários. Eles são separados por vírgula.
"""

# [1] Refatorando uma função: 

# Exemplo 1:--------------------------------------------------------------------------------------------

    # função da (Aula passada)
def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

    # Função Refatorada:  Obs: Agora a função recebe um parâmetro de entrada (Obrigatório)
def quadrado_de(numero):
    return numero ** 2

print(quadrado_de())  # TypeError
print(quadrado_de(20))
print(quadrado_de(9))

# Exemplo 2:--------------------------------------------------------------------------------------------

    # função da (Aula passada)
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

    # Função Refatorada:
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Doug')

# Exemplo 3:--------------------------------------------------------------------------------------------

def soma(a, b):
    return a + b

def multiplica(num1 , num2):
    return num1 * num2

def outra(num1, a, msg):
    return (num1 + a) * msg

soma(5, 5)
multiplica(5, 5)
outra(5, 5, 'Doug ')  # Se informarmos um número errado de parâmetro ou argumentos, teremos um TypeError

# -------------------------------------------------------------------------------------------------------

# [2] Nomeando parâmetros: Utilize nomes que façam sentido para seus parâmetros na hora de definir a função

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

nome_completo('Matheus', 'Menezes')

# [3] Diferenciando Parâmetros de Argumentos:

    # Parâmetros são variáveis declaradas na definição de uma função;
    # Argumentos são dados passados durante a execução de uma função.

    # Obs: A ordem dos parâmetros importa!

# [4] Argumentos nomeados: (Keyword Arguments)

    # Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
    # Nomear um argumento com o nome do parâmetro é utilizar chaves/Key, por isso podemos utilizar qualquer ordem;

# Exemplo:

nome = 'Matheus'
sobrenome = 'Menezes'

nome_completo(nome='Matheus', sobrenome='Menezes')
nome_completo(nome=nome, sobrenome=sobrenome)
nome_completo(nome=sobrenome, sobrenome=nome)

# -------------------------------------------------------------------------------------------------------

# [5] Erro comum na utilização do return:

def soma_impares(lista_de_numeros):
    total = 0
    for num in lista_de_numeros:
        if num % 2 != 0:
            total = total + num
#        return total  # Obs: O return não pode está contido no if, e sim fora do bloco do for
    return total


soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])