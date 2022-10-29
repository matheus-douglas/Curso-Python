# Range:
"""
 - Precisamos conhecer o loop for para usar os ranges;
 - precisamos conhecer o range para trabalha melhor com loops for.

Range são utilizados para gerar sequências numéricas, não de forma aleatória;

-> Formas gerais:

Forma[1] - range(valor_de_parada)
obs: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

Forma[2] - range(valor_de_inicio, valor_de_parada)
obs: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo de 1 em 1)

Forma[3] - range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada não inclusive (valor_de_inicio e passo especificado pelo usuário)

Forma[4] - range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada não inclusive (valor_de_inicio e passo especificado pelo usuário)
"""
# Exemplo[1]:
for num in range(11):
    print(num)
# Exemplo[2]:
for num in range(2, 11):
    print(num)
# Exemplo[3]:
for num in range(2, 11, 2):
    print(num)
# Exemplo[4]:
for num in range(11, 2, -2):
    print(num)
