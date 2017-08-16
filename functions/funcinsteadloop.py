def printsome(v):
    print(v)
    return v
    
lst = [1,3,7,2,4,5,8,6,9]
   
m = map(printsome, lst)
print(list(m))

print()

do_it = lambda f, *v: f(*v)
m = map(do_it, [printsome, printsome, printsome], [55, 77, 99])
print(list(m))

hello = lambda first, last: print("Hello", first, last)
bye = lambda first, last: print("Bye", first, last)
_ = list(map(do_it, [hello, bye], ['Davi', 'Jane'], ['Mertz', 'Doe']))
#print(_)

do_all_func = lambda fns, *v : [list(map(fn, *v)) for fn in fns]
_ = do_all_func([hello, bye], ['Davi', 'Jane'], ['Mertz', 'Doe'])
#print(_)
