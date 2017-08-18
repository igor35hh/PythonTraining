
class Adder():
    def __init__(self,n):
        self.n = n
    def __call__(self,m):
        return self.n + m
    
def make_adder(n):
    def adder(m):
        return m + n
    return adder

add_i = Adder(5)
add_f = make_adder(5)

print(add_i(5), add_f(5))

from multipledispatch import dispatch

@dispatch(int, int)
def add(x, y):
    return x + y

@dispatch(object, object)
def add(x, y):
    return "%s + %s" % (x, y)

print(add(1, 2))
print(add(1, 'hello'))

