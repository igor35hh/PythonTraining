from collections.abc import Iterable
class Fibonacci(Iterable):
    def __init__(self):
        self.a, self.b = 0, 1
        self.total = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.total += self.a
        return self.a
    def running_sum(self):
        return self.total
    
fib = Fibonacci()
print(fib.running_sum())
for _, i in zip(range(10), fib):
    print(i, end=" ")
print()
print(fib.running_sum())
print(next(fib))
print()

from itertools import tee, accumulate

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b
        
s, t = tee(fibonacci())
pairs = zip(t, accumulate(s))
for _, (fib, total) in zip(range(7), pairs):
    print(fib, total)


