from threading import Thread
import time
def foo(bar):
    print ('hello {0}'.format(bar))
    return "foo"

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        x = True
        while x:
            if self._target is not None:
                self._return = "3444"
            time.sleep(2)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

twrv = ThreadWithReturnValue(target=foo, args=('world!',))

twrv.start()
print (twrv.join())