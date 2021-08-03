"""
PEP - Python Enchancement Poposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A idéia da PEP8 é escrevermos códigos de formas Pythonica.

[1] Utilize Camel Case para nomes de section_5:
    class Calculadora / class CalculadoraCientifica

[2] Utilize nome em minúsculo separado por underline para funções ou variáveis:
    def soma() / def soma_dois()
    numero = 4 / numero_impar = 3

[3] Utilize quatro espaços para identação!

[4] Linhas em branco:
    Separar funções e definições de classe com duas linhas em branco;
    Métodos dentro de uma classe devem ser separados com uma única linha em branco.

[5] Imports
    Imports sempre devem ser feitos em linhas separadas!
    - import sys
    - import os
Não há problema em utilizar:
    - from types import StringType, ListType
Caso tenham muitos imports do mesmo pacote é recomendado fazer:
    - from Types import(
        StringType
        ListType
        SetType
        OutoType
    )
Imports devem ser colocados no topo de qualquer arquivo, logo depois de quaisquer comentários ou docstrings e antes de
constantes ou variáveis globais.

[6] Espaços em expressões e instruções:

Não faça:
    funcao( algo[ 1 ], { outro: 2 } )
Faça:
    funcao(algo[1], {outro: 2})

[7] Termine sempre uma instrução com uma nova linha.

"""
