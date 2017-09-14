from time import time, sleep as sys_sleep
from collections import deque

pending = deque()

class coroutine():
    _current = None

    def __init__(self, callable):
        self._callable = callable

    def __call__(self, *args, **kwargs):
        corogen = self._callable(*args, **kwargs)
        cls = self.__class__
        if cls._current is None:
            try:
                cls._current = corogen
                next(corogen)
            finally:
                cls._current = None
        return corogen
    
def sleep(timeout):  
    sys_sleep(timeout)
    revent = yield
    return revent

@coroutine
def hello(name, timeout):
    while True:
        yield from sleep(timeout)
        print("Hello, {}!".format(name))

a = hello("Igro", 2.0)
pending.append([a, time() + 2.0])
#a.send("timeout")
#a.__next__()
a = hello("Petro", 3.0)
pending.append([a, time() + 3.0])
#a.send("timeout")
#a.__next__()
a = hello("Nice", 5.0)
pending.append([a, time() + 5.0])
#a.send("timeout")
#a.__next__()

pending = deque(sorted(pending, key=lambda a: a[1]))
while len(pending) > 0:
    while len(pending) > 0:
        if pending[0][1] <= time():
            corogen, _ = pending.popleft()
            try:
                corogen.send("timeout")
            except StopIteration:
                pass
            else:
                break

