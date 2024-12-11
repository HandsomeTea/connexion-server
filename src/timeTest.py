import threading
import random
import time


class Timer:
    def __init__(self):
        self.record = {}

    def set_interval(self, interval: int, fn, **fnArgs):
        mark = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 10))

        def _set_interval(_mark, _interval: int, _fn, **_fnArgs):
            def wrapper():
                _set_interval(None, _interval, _fn, **_fnArgs)
                _fn(**_fnArgs)
            if (_mark):
                self.record[_mark] = threading.Timer(_interval, wrapper)
                self.record[_mark].start()
            elif (self.record[mark]):
                self.record[mark] = threading.Timer(_interval, wrapper)
                self.record[mark].start()

        _set_interval(mark, interval, fn, **fnArgs)
        return mark

    def clear_interval(self, timer):
        print('clear_interval: ', timer)
        if self.record[timer]:
            self.record[timer].cancel()
            self.record.pop(timer)


def task(arg: str):
    print("task excute with arg: ", arg)


timer = Timer()
__tag = timer.set_interval(2, task, arg='aaaaa')

print('__tag', __tag)
time.sleep(9)
timer.clear_interval(__tag)
