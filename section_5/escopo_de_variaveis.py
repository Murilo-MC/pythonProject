"""
Escopo de variáveis

1 - Variáveis globais;
    - São reconhecidas globalmente, ou seja, seu escopo compreende, TODO O PROGRAMA.

2 - Variáveis locais;
    - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo é limitado ao
    bloco onde foi declarada.

Para declarar variáveis em Python fazemos:
    - nome_da_variavel = valor_da_variavel

Lembrando que Python é uma linguagem de tipagem dinâmica;
    (Não declaramos o tipo de dado da variável);
    (O tipo é inferido ao atribuirmos o valor á mesma).

Exemplos :

C:
    int numero = 41;

Java:
    int numero = 42;

"""

numero = 42  # Variável Global
print(numero)
print(type(numero))

numero = 'Batman'
print(numero)
print(type(numero))

numero = 41
# novo = 0 - Variável Global

if numero > 10:
    novo = numero + 10 # 'novo' - Variável Local dentro do bloco 'if'.
    print(novo)

