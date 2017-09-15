from time import time
from collections import deque

current = deque()
IOLoop = deque()

class sleep(object):

    def __init__(self, timeout):
        self.deadline = time() + timeout

    def __await__(self):
        def swith_to(coro):
            current.append(coro)
            coro.send(time())
        IOLoop.append([self.deadline, swith_to, current[0]])
        current.pop()
        return (yield)
    
def coroutine_start(run, *args, **kwargs):
    coro = run(*args, **kwargs)
    current.append(coro)
    coro.send(None)
     
async def hello(name, timeout):
    while True:
        now = await sleep(timeout)
        print("Hello, {}!\tts: {}".format(name, now))
            
coroutine_start(hello, "Friends", 1.0)
coroutine_start(hello, "World", 2.5)

pending = deque(sorted(IOLoop, key=lambda a: a[0]))
while len(pending) > 0:
    while len(pending) > 0:
        if pending[0][0] <= time():
            tm, sw, args = pending.popleft()
            sw(args)
            print(tm, sw, args)

    

            