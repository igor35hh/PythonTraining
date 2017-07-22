class Stack(list):
    
    def top(self):
        return self[-1]
    
    def push(self, item):
        list.append(self, item)
        
    def pop(self):
        if not self:
            return None
        else:
            return list.pop(self)
        
class Set(list):
    def __init__(self, value=[]):
        list.__init__(self)
        self.concat(value)
        
    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)
    
    def union(self, other):
        res = Set(self)
        res.concat(other)
        
    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)
                
    def __and__(self, other):
        return self.intersect(other)
    
    def __or__(self, other):
        return self.union(other)
    
    def __str__(self):
        return '<Set:>' + repr(self) + '>'
    
class FastSet(dict):
    pass

def selfTest():
    stk = Stack()
    print(stk)
    for c in 'spam':
        stk.push(c)
    print(stk, stk.top())
    while stk:
        print(stk, stk.pop())
    print(stk, stk.pop())
    print()
    set = Set('spam')
    print(set, 'p' in set)
    print(set & Set('slim'))
    print(set | 'slim')
    print(Set('slim') | Set('slim'))
    print()
    stk = Stack('spam')
    print(stk)
    stk.insert(1, 'X')
    print(stk)
    stk.sort()
    print(stk)
    print()
    set = Stack('spam')
    set.reverse()
    print(set, set[1])
    
if __name__ == '__main__':
    selfTest()