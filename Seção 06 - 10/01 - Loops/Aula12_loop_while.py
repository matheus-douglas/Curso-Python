# Loop while

"""
Forma geral:

while expressão_booleana:
    //execução do loop

Obs: o bloco do while será repetido enquanto a expressão booleana for verdadeira(True).
 -> expressão booleana é toda expressão onde o resultado for verdadeiro ou falso. (Ture) or (False);

"""
# -> Exemplo[1]:
NUMERO = 1

while NUMERO < 10:
    print(NUMERO)
    NUMERO = NUMERO + 1
# Obs: Em um loop while, é importante que cuidemos do critário de parada,
# para não causar um loop infinito.

# -> Exemplo[2]:
RESPOSTA = ''

while RESPOSTA != 'sim':
    RESPOSTA = input('Já acabou? ')
