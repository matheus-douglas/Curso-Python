# Funções com parâmetros padrão -> Default Paramters

# - Funções onde a passagem de parâmetro seja opcional;

#----------------------------------------------------------------------------------------------------------------------------------
# [1] Exemplo de função onde a passagem de parâmetros seja opcional:
print()

#----------------------------------------------------------------------------------------------------------------------------------
# [2] Exemplo de função onde a passagem de parâmetros seja obrigatoria:

def quadrado(num):
    return num ** 2


def exponencial(numero, potencia):
    return numero ** potencia

exponencial(2, 5)

#----------------------------------------------------------------------------------------------------------------------------------
# [3] Podemos facilmente definir um parâmetro padrão caso o usuário não o informe, tornando o parâmetro opcional:

def exponencial(numero, potencia=2):
    return numero ** potencia

exponencial(3, 5)  # Eleva á potencia informada pelo usuário

exponencial(3)  # Eleva ao padrão definido na função

# Obs: Se o usuário passar somente 1 parâmetro, este será atribuido ao parâmetro numero, e será calculado o quadrado deste número
# Se o usuário passar 2 parâmetros, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potência. então será
# Calculado esta potência

#----------------------------------------------------------------------------------------------------------------------------------
# [4] Em Python, os parâmetros com valores defaut (padrão) DEVEM sempre está ao final da declaração:

"""
# ERROR:

def test(num=2, potencia):
    return num ** potencia

print(test(5))

"""
#----------------------------------------------------------------------------------------------------------------------------------
# (1) Outros exemplos:


def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  # TypeError
print()  # TypeError

#----------------------------------------------------------------------------------------------------------------------------------
def mostra_informacao(nome='Doug', instrutor=False):
    if nome =='Doug' and instrutor:
        return f'Bem-vindo instrutor {nome}'
    elif nome == 'Doug':
        return f'Pensei que você fosse instrutor {nome}'
    return f'Olá {nome}'

print(mostra_informacao('Doug', True))
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Matheus'))
print(mostra_informacao())

#----------------------------------------------------------------------------------------------------------------------------------

# [5] Por quê utilizar parâmetros com valor Default?

# - Nos permite ser mais flexíveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legíveis de códigos

#----------------------------------------------------------------------------------------------------------------------------------
# [6] Quais tipos de dados podemos utilizar como valores default para parâmetros?

# - Qualquer tipo de dado:
#   - Números, Strings, Floats, Booleanos, Listas, Tuplas, Dicionários, Funções e etc...;

#----------------------------------------------------------------------------------------------------------------------------------
# [7] Passando uma função como parâmetro:

def soma(num1, num2):  # Função soma padrão
    return num1 + num2

def subtracao(num1, num2):  # Função subtração padrão
    return num1 - num2

def mat(num1, num2, fun=soma):  # Função que recebe outra função como parâmetro
    return fun(num1, num2)

print(mat(2, 3))
print(mat(2, 2, subtracao))

#----------------------------------------------------------------------------------------------------------------------------------
# [8] Escopo: (Evitar problemas e confusões...)

#   - Variáveis globais
#   - Variáveis locais

instrutor = 'DOUG'  # Variável global

def diz_oi():
    return f'Oi {instrutor}'

print(diz_oi())

def diz_oi():
    instrutor = 'Matheus'  # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# Obs: Se tivermos uma variável local com o mesmo nome de uma variável global, á local terá sempre preferência;
# Obs: A variável local só existe dentro do bloco onde foi definida;

#----------------------------------------------------------------------------------------------------------------------------------
# [9] ATENÇÂO com variáveis globais: (Se possível as evite!)

total = 0  # Variável global

def incremento():
    total = total + 1  # UnboundLocalError -> A variável local está sendo utilizada para processamento sem ter sido inicializada
    return total

print(incremento())  # UnboundLocalError

#   -> REFATORANDO:

total = 0

def incremento():
    global total  # Avisando ao Python que queremos utilizar a variável global
    total = total + 1
    return total

print(incremento())
print(incremento())
print(incremento())

#----------------------------------------------------------------------------------------------------------------------------------
# [10] Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável:

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
    
print(fora())
print(fora())
# print(dentro()  # NameError -> A função dentro() não é conhecida fora do escopo da função fora()
