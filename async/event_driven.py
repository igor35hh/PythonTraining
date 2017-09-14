from collections import deque
from time import time, sleep as sys_sleep

class Dispatcher():
    """Dispatcher of events"""
    def __init__(self):
        self._pending = deque()
        self._deadline = time() + 3600.0

    def setup_timeout(self, corogen, timeout):
        deadline = time() + timeout
        self._deadline = min([self._deadline, deadline])
        self._pending.append([corogen, deadline])
        self._pending = deque(sorted(self._pending, key=lambda a: a[1]))

    def run(self):
        """loop of events"""
        while len(self._pending) > 0:
            timeout = self._deadline - time()
            self._deadline = time() + 3600.0
            if timeout > 0:
                sys_sleep(timeout)
            while len(self._pending) > 0:
                if self._pending[0][1] <= time():
                    corogen, _ = self._pending.popleft()
                    try:
                        coroutine._current = corogen
                        corogen.send("timeout")
                    except StopIteration:
                        pass
                    finally:
                        coroutine._current = None
                else:
                    break

class coroutine():
    """makes function as coroutine, it based on extension of generator"""
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
    """waiting for event"""
    corogen = coroutine._current
    dispatcher.setup_timeout(corogen, timeout)
    revent = yield
    return revent
        
@coroutine
def hello(name, timeout):
    while True:
        yield from sleep(timeout)
        print("Hello, {}!".format(name))

dispatcher = Dispatcher()
run = lambda: dispatcher.run()

hello("Igo", 2.0)
hello("Petro", 3.0)
hello("Nice", 5.0)

run()
