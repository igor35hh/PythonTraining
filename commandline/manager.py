
from Person import Person

class Manager(Person):
    
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'mahager')
    
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
        
if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=5000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    
    bob = Person(name='Bob Smith', age=42, pay=3000)
    sue = Person(name='Sue Jones', age=45, pay=4000)
    
    db = {bob, sue, tom}
    
    for obj in db:
        obj.giveRaise(.30)
        
    for obj in db:
        print(obj.lastName(), '=>', obj.pay)
        print(obj)
        
    for d in obj.__dict__:
        print(obj.__dict__[d]);
        
    for v in obj.__dict__.values():
        print(v);