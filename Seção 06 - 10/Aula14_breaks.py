# Saindo de loops com o break

"""
Funciona da mesma forma que nas linguagens C e Java;

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo [1]: -> com for

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sair do loop')

# Exemplo [2]: -> com while

while True:
    COMANDO = input("Digite 'sair' para sair: " )
    if COMANDO == 'sair':
        break
