import time
m = dict()

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range (2, n+1):
        res = a + b
        a, b = b, res
    return res
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
        return m[n]

n = 20
start = time.time()
print(fib_rec(n))
print('Recursive: {} seconds'.format(time.time() - start))
start = time.time()
print(fib_it(n))
print('Iteratie: {} seconds'.format(time.time() - start))
print(fib_mem(n))
print('Memoization: {} seconds'.format(time.time() - start))
'''def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n -1) + fib(n-2)
if __name__ == "__main__":
    print(fib(5))
    print(fib(10))'''
