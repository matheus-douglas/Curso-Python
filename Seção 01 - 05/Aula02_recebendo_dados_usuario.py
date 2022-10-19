"""
    Recebendo_dados_do_usuário

input() -> Todo dado recebido via input é do tipo string

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas.



# Entrada de dados: (input)
print("Qual seu nome?")
nome = input()



# Entrada de dados: (input) Melhorado
nome = input('Qual seu nome? ')



# Saída 'antiga' -> python 2.x
print('Seja bem-vindo(a) %s' % nome)

# Saída 'moderna' -> python 3.x
print('Seja bem-vindo(a) {0}' .format(nome))

# Saída 'Atual' -> python 3.7+
print(f'Seja bem-vindo(a) {nome}')



# Entrada de dados: (input)
print("Qual sua idade?")
idade = input()



# Entrada de dados: (input) Melhorado
idade = input('Qual dsua idade? ')



# Saída 'antiga' -> python 2.x
print('O Sr(a) %s tem %s anos' % (nome, idade))

# Saída 'moderna' -> python 3.x
print("O Sr(a) {0} tem {1} anos" .format(nome, idade))

# Saída 'Atual' -> python 3.7+
print(f'O senhor {nome} tem {idade} anos')


# int(idade) -> Cast
# Cast é a 'conversão' de um tipo de dado para outro


# Cast feito na saida
nome = input('Qual seu nome? ')
idade = input ('Qual sua idade? ')
print(f'O Sr(a) {nome} nasceu em {2022 - int(idade)}')


# Cast feito já no input
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
print(f'O(a) Sr(a) {nome} nasceu em {2022 - idade}')
"""
