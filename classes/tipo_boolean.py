"""
Tipo booleano - Algebra, criador George Boole.

Consiste em 2 constantes, Vedadeiro(True) ou Falso(False).

Obs: Sempre com a inicial maiuscula.
"""

ativo = True

print(ativo)

"""
Operações básicas:
"""
# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso.
Se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# Ou (orr):
"""
Operação binária, pois depende de dois valores. Um OU outro deve ser verdadeio.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária. Neste caso ambos os valoes devem ser verdadeiros(True).

True and True -> True
True and False -> False
False and True -> False
False and False -> True
"""
