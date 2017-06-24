import shelve
from Person import Person

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    
    if not key:
        break
    
    if key == 'edit':
        keyedit = input('\nKey edit? => ')
        
        if keyedit in db:
            record = db[keyedit]
        else:
            record = Person(name='?', age='?')
        
        for field in fieldnames:
            currval = getattr(record, field)
            newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
            print(newtext)
            if newtext:
                setattr(record, field, eval(newtext))
        db[keyedit] = record
    
    if key == 'exit':
        db.close()
        raise SystemExit(1)
    
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
          
    
    