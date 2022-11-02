# Map

"""
-> Com map, fazemos mapeamento de valores para função.
-> Map é uma função que recebe dois parâmetros:
    - O primeiro: A função
    - O segundo: Um iterável
-> Após utilizar a função map():
    - Após a primeira utilização do resultado do map(), ele é zerado automaticamente;
-> A função utilizada dentro do map, so pode receber um (01) parâmetro.
"""
import math


# Função area do circulo
def area(r):
    """Calcula a area de um circulo com o raio 'r'."""
    return math.pi * (r ** 2)

area(4)
print(f'{area(4):,.2f}')

# Exemplo [1]: Calculando varios raios

raios = [2, 5, 7.1, 0.3, 10, 44]

    # Forma comum:
areas1 = []
for r in raios:
    areas1.append(f'{(area(r)):,.2f}')

print(areas1)

    # Forma 02- utilizando Map

areas2 = map(area, raios)

print(list(areas2))

# Exemplo [02]: Refatorando a função area usando lambda (Map + Lambda)

raios = [2, 5, 7.1, 0.3, 10, 44]

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Fixação do Map:

# Temos que ter dados iteráveis:
#   - dados = a1, a2, a3, a4, ..., an list,set,tuple
# Temos que ter uma função:
#   - def f(x):

# -> Utilizamos a função Map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função
# Map Object: f(a1), f(a2), f(....) f(an)

# Exemplo de fixação: Conversão de temperatura

cidades_graus = [('Berlim', 29), ('Cario', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
 ('Nova York', 28), ('Londres', 22)]

# Conversão de graus celsius para fahrenheit: C = celsius / F = fahrenheit
#   F = 9/5 * C + 32

C_para_F = lambda dado: (dado[0], f'{((9/5) * dado[1] + 32):,.2f}')  # Delimitando 2 casas decimais
C_para_F = lambda dado: (dado[0], round((9/5) * dado[1] + 32))  # Arredondando o resultado

#    (lista(map(funçao , valores iteraveis)))
print(list(map(C_para_F, cidades_graus)))
