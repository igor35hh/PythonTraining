import time, os, sys
from multiprocessing import Process
from socket import *

myHost = ''
myPort = 3000

def now():
    return time.ctime(time.time())
        
def handleClient(connection):
    print('Ch:', os.getpid())
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    
def dispatcher():
    while True:
        connection, adress = sockobj.accept()
        print('Server connected by', adress, end=' ')
        print('at', now())
        Process(target=handleClient, args=(connection,)).start()
            
if __name__ == '__main__':
    print('P:', os.getpid())
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((myHost, myPort))
    sockobj.listen(5)
    dispatcher()
    