"""
Tipo Numérico -> Inteiro

---------------
# Exp:
1000
23
485
30000
...
---------------


Tipo Real/Decimal -> Float

 --------------
# Exp:
 22,5
 14,6
 74,3
 51,2
 ...
 ---------------

# OBS: O separador de casas decimais é o ponto (.) e não a vírgula (,).

# Errado:
1,44
# Certo:
1.44
"""

# Errado: do ponto de vista do float mas gera uma tupla
VALOR = 1, 44
print(VALOR)
print(type(VALOR))

# Certo: do ponto de vista do float
VALOR = 1.44
print(VALOR)
print(type(VALOR))

# Possivel: dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int:
# OBS: Ao converter (usar o cast) valores float para int, perdemos precissão.
RES = int(VALOR)
print(RES)
print(type(RES))


# OBS:
# Para trabalhar com numeros complexos, devemos adicionar a letra (j) após o numero
# dentro da variável.
