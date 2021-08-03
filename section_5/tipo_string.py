"""
Tipo String

Em Python, um dado é considerado do tipo String sempre que:

- Estiver entre áspas simples -> 'uma string';
- Estiver entre áspas duplas -> "2345"
- Estiver entre áspas simples triplas -> '''True'''
- Estiver entre áspas duplas triplas...

# Aplicando as áspas:
nome = "How to code"
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'New \nYork'
print(nome)
print(type(nome))
# Ou

nome = 'New York'
print(nome)
print(type(nome))

print(nome.upper())
print(nome.lower())
print(nome.split()) # Transforma em lista
print(nome[0:4]) #(Slice de string) exibe a seleção dos caracteres 0 ao 3. 
print(nome.split()[0])
print(nome[::-1]) # Inversão da String
"""

texto = 'socoram me subino onibus em marrocos'
print(texto)

print(texto[::-1])
