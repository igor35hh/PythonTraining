import shelve
from Person import Person
from manager import Manager


bob = Person('Bob Smith', 42, 3000, 'software')
sue = Person('Sue Jones', 45, 4000, 'hardware')
tom = Manager('Tom Doe', 50, 5000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)
    
bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
