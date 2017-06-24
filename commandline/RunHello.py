from macpath import split

bob = ['Bob', 42, 3000, 'software']
sue = ['Sue', 45, 4000, 'hardware']

print(bob[0])
print(sue[2])

fam = bob[0].split()[0]
print(fam)

sue[2] *= 1.25
print(sue[2])

people = [bob, sue]
print(people)
for person in people:
    print(person)
    
print(people[1][0])

for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20
    
for person in people:
    print(person[2])
    
pays = [person[2] for person in people]
print(pays)

pays = map((lambda x: x[2]), people)
print(list(pays))

print(sum(person[2] for person in people)) # generator

people.append(['Tom', 50, 0, None])
print(len(people))

print(people[-1][0])

NAME, AGE, PAY = range(3)
print(bob[NAME])

bob = [['name', 'Bob'], ['age', 42], ['pay', 1000]]
sue = [['name', 'Sue'], ['age', 45], ['pay', 2000]]
people = [bob, sue]

for person in people:
    print(person[0][1], person[2][1])

for person in people:
    print(person[0][1].split()[-1])
    person[2][1] *= 1.10
    
for person in people:
    print(person[2])
    
for person in people:
    for (name, value) in person:
        if name == 'name' : print(value)
        
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue

print(field(bob, 'name'))
print(field(bob, 'pay'))

for rec in people:
    print(field(rec, 'age'))
    
# dictioanary
    
bob = {'name':'Bob Smith', 'age':42, 'pay':3000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':4000, 'job':'hdw'}

print(bob['name'], sue['pay'])

print(bob['name'].split()[-1])

sue['pay'] *= 1.10

print(sue['pay'])

bob = dict(name='Bob Smoth', age=42, pay=3000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=4000, job='hdw')

print(bob)

sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 4000
sue['job'] = 'hdw'

print(sue)

names = ['name', 'age', 'pay', 'job']
values = ['Sue Jonson', 45, 4000, 'hdw']
l = list(zip(names, values))
print(l)

sue = dict(zip(names, values))
print(sue)

fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
print(record)

people = [bob, sue]
for person in people:
    print(person['name'], person['pay'], sep=', ')
    
for person in people:
    if person['name'] == 'Sue Jonson':
        print(person['pay'])
        
names = [person['name'] for person in people]
print(names)

l = list(map((lambda x: x['name']), people))
print(l)

s = sum(person['pay'] for person in people)
print(s)

r = [rec['name'] for rec in people if rec['age'] >= 45]
print(r)

r = [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
print(r)

def f(*a):
    print(a)
    
f(1, 'ddd')

g = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(g))

g = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(g.__next__())

for person in people:
    print(person['name'].split()[-1])
    person['pay'] *= 1.10

for person in people:
    print(person['pay'])
    
a = {'a':1, 'b':2}
b = {'a':3, 'c':0}
c = {**a, **b}
print(c)

# nested srtuctures

bob2 = {'name': {'first':'Bob', 'last':'Smith'}, 'age':42, 'job':['software', 'writing'], 'pay':(4000, 5000)}
print(bob2['name'])
print(bob2['name']['last'])
print(bob2['pay'][1])

for job in bob2['job']:
    print(job)

print(bob2['job'][-1])

bob2['job'].append('janitor')
print(bob2)

bob = dict(name='Bob Smith', age='42', pay=3000, job='dev')
sue = dict(name='Sue Jones', age='45', pay=4000, job='hdw')

db = {}
db['bob'] = bob
db['sue'] = sue

print(db['bob']['name'])
db['sue']['pay'] = 5000
print(db['sue']['pay'])

print(db)

import pprint
pprint.pprint(db)

for key in db:
    print(key, db[key]['name'])
    print(key, db[key]['pay'])
    
for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10
    
for record in db.values():
    print(record['pay'])
    
x = [db[key]['name'] for key in db]
print(x)

x= [rec['name'] for rec in db.values()]
print(x)

db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print(db['tom'])
print(db['tom']['name'])
print(len(db))

r = [rec['age'] for rec in db.values()]
print(r)

r = [rec['name']  for rec in db.values() if int(rec['age'])>45]
print(r)
