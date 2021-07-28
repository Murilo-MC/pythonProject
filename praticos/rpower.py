def rpower(a, n):
    'retorna a á potência n'
    global counter
    if n == 0:
        return 1
    tmp = rpower(a, n//2)
    if n % 2 == 0:
        counter +=1
        return tmp*tmp
    else:
        counter +=2
        return a*tmp*tmp