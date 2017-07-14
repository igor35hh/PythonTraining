import time, sys
from select import select
from socket import socket, AF_INET, SOCK_STREAM

myHost = ''
myPort = 3000

if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2

def now():
    return time.ctime(time.time())

mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
    sockport = socket(AF_INET, SOCK_STREAM)
    sockport.bind((myHost, myPort))
    sockport.listen(5)
    mainsocks.append(sockport)
    readsocks.append(sockport)
    myPort += 1
    
print('select-server loop starting')
while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            newsock, adress = sockobj.accept()
            print('Connect:', adress, id(newsock))
            readsocks.append(newsock)
        else:
            data = sockobj.recv(1024)
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply = 'Echo=>%s at %s' % (data, now())
                sockobj.send(reply.encode())
    
    
    