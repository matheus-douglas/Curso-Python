# Definindo funções:

"""
- Funções são pequenas partes de código que realizam tarefas específicas;
    - Pode ou não receber entrada de dados e retornar uma saída de dados;
    - São muito uteis para executar procedimentos similares repetidas vezes;
    - DRY: Don't Repeat Yourself -> Não repita você mesmo / Não repita seu código

Obs: Se você escrever uma função que realize várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

já utilizamos várias funções desde que iniciamos este curso:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e diversas outra...

--------------------------------------------------------------------------------------------------

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

CURSO = 'Programação em Python'

# Utilizando uma função integrada (built-in) do Python:

    # [1] print()

print(cores)

print(CURSO)

    # [2] .append()

cores.append('roxo')

# CURSO.append('Mais dados...') -> Gera um AttributeError
# Obs: O tipo Str (string) não recebe a função .append()

    # [3] .clear()

cores.clear()
print(cores)

# CURSO.clear() -> Gera um AttributeError
# Obs: O tipo Str (string) não recebe a função .clear()
# Obs: A função .clear() não recebe dados de entrada

--------------------------------------------------------------------------------------------------

-> Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao

onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, se for nome composto, separado por underline;

parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo
ser opcionais ou não;

bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da
função acontece; Nesse bloco, pode ter ou não retorno da função.

# Obs: Veja que para definir uma função, utilizamos a palavra reservada 'def',
informando ao Python que estamos definindo uma função. Tambpem abrimos o bloco de código com o já
conhecido dois pontos : que é utilizado em Python para definir blocos, com a linha seguinde identada
com 4 (quatro) espaços.

"""

# Definindo a primeira função:

   # [1] Exemplo 1:

def diz_oi():
    print('oi!')

# Obs:
    # 1 - Veja que, dentro das nossas funções podemos utilizar outras funões;
    # 2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
    # 3 - Veja que esta função não recebe nenhum parâmetro de entrada;
    # 4 - Veja que esta função não retorna nada.

    # [2] Exemplo 2:

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


# Utilizando a função: ATENÇÂO -> Nunca esqueça de utilizar o parênteses ao executar uma função

diz_oi()  # Executando o exemplo 1

cantar_parabens()  # Executando o exemplo 2

# Podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

# Exemplo:

canta = cantar_parabens

canta()

# Obs: Não é comum, mas é possível.
