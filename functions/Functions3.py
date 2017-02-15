import datetime

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}!"""

def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.year}/{today.year}'.format(today=today)
        for name in names:
            
            name = name[0].upper() + name[1:].lower()
            
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(name=name, date=text, total=new_amount)
            i += 1
            print(new_msg)
            
make_messages(default_names, default_amounts)