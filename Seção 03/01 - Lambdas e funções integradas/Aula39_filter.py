# Filter

"""
filter() serve para filtrar dados de uma certa coleção.

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utlizando a função meam():
media = statistics.mean(dados)

print(f'Media: {(media):,.2f}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros,
# sendo uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))
print(type(res))

# OBS: Assim como na função map() após serem utilizados os dados de 
# filter() eles são excluidos da memória.

# -----------------------------------------------------------------------

# Remoção de dados faltantes:

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

# Froma (01):
res1 = filter(None, paises)
print(list(res1))

# Forma (02):
res2 = filter(lambda pais: len(pais) > 0, paises)
print(list(res2))

# Forma (03):
res3 = filter(lambda pais: pais != '', paises)
print(list(res3))
