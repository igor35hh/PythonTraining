def factorialR(N): #recursive
    assert isinstance(N, int) and N >= 1
    return 1 if N <= 1 else N * factorialR(N-1)

def factorialI(N): #iterative
    assert isinstance(N, int) and N >= 1
    product = 1
    while N >= 1:
        product *= N
        N -= 1
    return product

from functools import reduce
from operator import mul

def factorialHOF(N):
    return reduce(mul, range(1, N+1), 1)

print(factorialR(5))

print(factorialI(5))

print(factorialHOF(5))

