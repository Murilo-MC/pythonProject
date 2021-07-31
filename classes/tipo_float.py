"""
Tipo Float

Tipo real/decimal
Casas decimais = O separador em programação é o ponto(US), não a virgula(BR).
"""

# Errado para Float, pois gera 'tuple'.
valor = 1, 44
print(valor)
print(type(valor))

# Certo para tipo Float.
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição.
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Converter Float para Int
"""
OBS: Ao converter Float para Int, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Números complexos
numC = 5j
res1 = numC ** 2
print(numC)
print(res1)
print(type(numC))
