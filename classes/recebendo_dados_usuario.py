"""
Recebendo dados do usuárrio

input() -> Todo dado recebido via input é do tipo String.
"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()
nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s!' % nome)
# Exemplo de print moderno 3.x
# print('Seja bem-vindo(a) {0}!'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}!')

# print("Qual sua idade? ")
# idade = input()
idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# print(' %s tem %s anos.' % (nome, idade))
# Exemplo de print moderno 3.x
# print('{0} tem {1} anos.'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'{nome} tem {idade} anos.')

# int(idade)
# Cast é a 'conversão' de um tipo de ddado para outro.
print(f'{nome} nasceu em {2021 - idade}')
