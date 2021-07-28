def pattern(n):
    'exibe o enésimo padrão'
    if n == 0:
        print(0, end='')
    else:
        pattern(n - 1)
        print(n, end='')
        pattern(n - 1)

'''def vertical(n): 'exibe dígitos de n verticalmente'
    if n < 10:  # caso básico: n tem 1 dígito
        print(n)  # apenas exibe n
    else:  # etapa recursiva: n tem 2 ou mais dígitos
        vertical(n // 10)  # exibe recursivamente todos, menos o último dígito
        print(n % 10)  # exibe último dígito de n'''