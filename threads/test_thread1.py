import thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))

def start_thread():
    try:
        thread.start_new_thread(print_time, ("Thread-1", 2, ))
        thread.start_new_thread(print_time, ("Thread-2", 4, ))
    except:
        print "Error: unable tp start thread"

    while 1:
        pass
