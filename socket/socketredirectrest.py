import sys, os, multiprocessing
from socketredirect import *

#redirect client output
def server1():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))
        
def client1():
    mypid = os.getpid()
    redirectOut()
    for i in range(3):
        print('client %s: %s' % (mypid, i))
        sys.stdout.flush()
     
#redirect client input   
def server2():
    mypid = os.getpid()
    conn = initListenerSocket()
    for i in range(3):
        conn.send(('server %s got [%s]' % (mypid, i)).encode())
        
def client2():
    mypid = os.getpid()
    redirectIn()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))
        
#redirect client input + output from socket client
def server3():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        conn.send(('server %s got [%s]\n' % (mypid, data)).encode())
        
def client3():
    mypid = os.getpid()
    redirectBothAsClient()
    for i in range(3):
        print('client %s got [%s]' % (mypid, i))
        data = input()
        sys.stderr.write('client %s got [%s]\n' % (mypid, data))
        
#redirect client input + output from socket server
def server4():
    mypid = os.getpid()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r')
    for i in range(3):
        sock.send(('server %s: %s\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))
        
def client4():
    mypid = os.getpid()
    redirectBothAsServer()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))  
        sys.stdout.flush() 
        
#redirect client input + output from socket client but server first
def server5():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        conn.send(('server %s: %s\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))
        
def client5():
    mypid = os.getpid()
    s = redirectBothAsClient()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))
        sys.stdout.flush()

if __name__ == '__main__':
    server = eval('server' + sys.argv[1])
    client = eval('client' + sys.argv[1])
    multiprocessing.Process(target=server).start()
    client()
