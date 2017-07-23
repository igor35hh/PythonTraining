from datastructures.setclass import Set

class RSet(Set):
    
    def list(self):
        print('\ntable =>')
        for x in self.data:
            for f in x.keys():
                print('[%s]=%r' % (f, x[f]), end=' ')
            print()
            
    def select(self, field, value):
        result = []
        for x in self.data:
            if x[field] == value:
                result.append(x)
        return RSet(result)
    
    def bagof(self, expr):
        res = []
        for X in self.data:
            if eval(expr):
                res.append(X)
        return RSet(res)
    
    def find(self, field, cmp, value):
        return self.bagof('X[%r] %s %r' % (field, cmp, value))
    
    def match(self, other, field):
        result = []
        for x in self.data:
            for y in other:
                if y[field] == x[field]:
                    result.append(x)
        return RSet(result)
    
    def join(self, other, field):
        result = []
        for x in self.data:
            for y in other:
                if y[field] == x[field]:
                    compos = self.copy_tuple(x)
                    for k in y.keys():
                        if k not in x:
                            compos[k] = y[k]
                    result.append(compos)
        return RSet(result)
    
    def product(self, other):
        result = []
        for x in self.data:
            for y in other:
                compos = self.copy_tuple(x)
                for k in y.keys():
                    if not k in x:
                        compos[k] = y[k]
                    else:
                        i = 1
                        while(k + '_' + repr(i)) in x:
                            i += 1
                        compos[k + '_' + repr(i)] = y[k]
                result.append(compos)
        return RSet(result)
    
    def project(self, fields):
        result = []
        for x in self.data:
            tuple = {}
            for y in fields:
                if y in x:
                    tuple[y] = x[y]
            if tuple and not tuple in result:
                result.append(tuple)
        return RSet(result)
    
    def copy_tuple(self, tup):
        res = {}
        for field in tup.keys():
            res[field] = tup[field]
        return res
    
    def input_table(self, fields):
        tup = {}
        for x in fields:
            valstr = input(x + ' => ')
            tup[x] = eval(valstr)
        self.data.append(tup)
    
    def difference(self, other):
        res = []
        for x in self.data:
            if x not in other:
                res.append(x)
        return RSet(res)
    
if __name__ == '__main__':
    
    def test():
        a  = RSet(
                [{'name':'marv',  'job':'engineer'},     
                 {'name':'andy',  'job':'engineer'},     
                 {'name':'sam',   'job':'manager'},      
                 {'name':'mary',  'job':'prez'},         
                 {'name':'mira',  'job':'architect'},   
                 {'name':'john',  'job':'engineer'},     
                 {'name':'eddy',  'job':'administrator'}]
            )
        
        b = RSet(
                [{'job':'engineer', 'pay':(25000,60000)},  
                 {'job':'manager',  'pay':(50000,'XXX')},  
                 {'job':'architect','pay':None},           
                 {'job':'prez',     'pay':'see figure 1'}]
            )
        
        c = RSet(
                [{'name':'marv',  'job':'engineer'},     
                 {'name':'andy',  'job':'engineer'},     
                 {'name':'sam',   'job':'manager'},      
                 {'name':'julie', 'job':'engineer'},     
                 {'name':'steve', 'job':'manager'}]
            )
        
        a.list()
        a.select('job', 'engineer').list()
        a.join(b, 'job').list()
        a.project(['job']).list()
        a.select('job', 'engineer').project(['name']).list()
        a.find('job', '>', 'engineer').list()
        c.find('job', '!=', 'engineer').list()
        a.bagof("X['name'][0] == 'm'").list()   
        a.bagof("X['job'] > 'engineer'").list()
        a.bagof("X['job'] > 'engineer' or X['name'] == 'eddy'").list()
        a.project(['job']).difference(b.project(['job'])).list()
        a.join(b, 'job').project(['name', 'pay']).list()
        a.select('name','sam').join(b,'job').project(['name', 'pay']).list()
        
    test()