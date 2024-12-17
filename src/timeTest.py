import threading
import random
import time


class Timer:
    def __init__(self):
        self.record = {}

    def set_interval(self, interval: int, fn, **fnArgs):
        timer_record = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 10))

        def _set_interval(_timer_record, _interval: int, _fn, **_fnArgs):
            def wrapper():
                _set_interval(None, _interval, _fn, **_fnArgs)
                _fn(**_fnArgs)
            if (_timer_record):
                self.record[_timer_record] = threading.Timer(_interval, wrapper)
                self.record[_timer_record].start()
            elif (self.record[timer_record]):
                self.record[timer_record] = threading.Timer(_interval, wrapper)
                self.record[timer_record].start()

        _set_interval(timer_record, interval, fn, **fnArgs)
        return timer_record

    def clear_interval(self, timer):
        print('clear_interval: ', timer)
        if self.record[timer]:
            self.record[timer].cancel()
            self.record[timer] = None
            self.record.pop(timer)


def task(arg: str):
    print("task excute with arg: ", arg)


timer = Timer()
__tag = timer.set_interval(2, task, arg='aaaaa')

print('__tag', __tag)
time.sleep(9)
timer.clear_interval(__tag)
