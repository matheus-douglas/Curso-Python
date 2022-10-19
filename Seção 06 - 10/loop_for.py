# Loop for

# Loop -> Estrutura de repetição
# for (para) -> Uma dessas estruturas

"""
# Exemplo em C ou Java:

for(int i= 0; i < 10; i++){
    //execução do loop
}

# Exemplo em python:

for item in interavel:
    //execução do loop

# Uilizamos os loops para iterar sobre sequências ou sobre valores iteráveis:

Exemplos de iteráveis:
- String
    nome = 'doug'
- Listas:
    listas - [1 ,3, 5, 7, 9]
- Range
    numeros = range(1, 10)
-------------------------------------------------------------------------------

nome = 'doug'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for[1]: iterando sobre uma string

for letra in nome:
    print(letra)

# Exemplo de for[2]: iterando sobre uma lista

for numero in lista:
    print(numero)

# Exemplo de for[3]: iterando sobre um range
# Range(valor_inicial, valor_final) obs: o valor final não é inclusive
for numero in range(1, 10):
    print(numero)

# Exemplo enumerate: 'doug' -> ((0, d), (1, o), (2, u), (3, g))
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
# Obs: quando não precisamos de um valor podemos descartá-lo utilizando um (_)
for valor in enumerate(nome):
    print(valor)

# Outros exemplos:

qtd = int(input('quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'doug'
for letra in nome:
    print(letra, end='')
"""

# Tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode

# emoji original: U+1F631
# emoji modificado: (para modificar, substitua o (+) por (000))

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F631' * num)
