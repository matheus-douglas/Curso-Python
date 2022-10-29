# Mapas -> Conhecidos em python como dicionários

"""
Dicionários em Python são representados por cahves {}

"""
# Exemplo:

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# iterar sobre dicionários:

    # Acessando as keys:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

for chave in receita.keys():
    print(receita[chave])


print(receita.items())
print(receita.keys())

    # Acessando os values:
print(receita.values())

for valor in receita.values():
    print(valor)

    # Desempacotamento de dicionários:
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

print(receita.items())

    # Soma, valor máximo*, valor mínimo*, tamanho*
        # * se os valores forem todos inteiros ou reais int/float;
print(sum(receita.values()))  # Soma
print(max(receita.values()))  # Valor Máximo
print(min(receita.values()))  # Valor Mínimo
print(len(receita))  # Tamanho
