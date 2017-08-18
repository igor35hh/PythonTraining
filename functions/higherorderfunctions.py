iterator = (0,1,2,3,4,5)

def transformation(x):
    return x * x

transformed1 = map(transformation, iterator)

transformed2 = (transformation(x) for x in iterator)

print(list(transformed1), list(transformed2))
print()

def predicate(x):
    if x > 2:
        return True
    return False

filtered1 = filter(predicate, iterator)

filtered2 = (x for x in iterator if predicate(x))

print(list(filtered1), list(filtered2))
print()

from functools import reduce

add5 = lambda n: n+5
r = reduce(lambda l, x: l+[add5(x)], range(10), [])
print(r)

isOdd = lambda n: n%2
rr = reduce(lambda l, x: l+[x] if isOdd(x) else l, range(10), [])
print(rr)

def compose(*funcs):
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner

times2 = lambda x: x*2; minus3 = lambda x: x-3; mod6 = lambda x: x%6
f = compose(mod6, times2, minus3)
result = all(f(i)==((i-3)*2)%6 for i in range(1000000))
print(result)



