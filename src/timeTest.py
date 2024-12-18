import threading
import asyncio
import random


class Timer:
    def __init__(self):
        self.timer_record = {}
        self.event_loop_record = {}

    def __generate_record_key(self):
        return ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 10))

    # 使用递归+threading实现定时器
    # def set_interval(self, interval: int, fn, **fn_args):
    #     timer_record = self.__generate_record_key()

    #     def _set_interval(_timer_record, _interval: int, _fn, **_fn_args):
    #         def wrapper():
    #             _set_interval(None, _interval, _fn, **_fn_args)
    #             _fn(**_fn_args)
    #         if (_timer_record):
    #             self.timer_record[_timer_record] = threading.Timer(_interval, wrapper)
    #             self.timer_record[_timer_record].start()
    #         elif (self.timer_record[timer_record]):
    #             self.timer_record[timer_record] = threading.Timer(_interval, wrapper)
    #             self.timer_record[timer_record].start()

    #     _set_interval(timer_record, interval, fn, **fn_args)
    #     return timer_record

    # def clear_interval(self, timer):
    #     print('clear_interval: ', timer)
    #     if self.timer_record[timer]:
    #         self.timer_record[timer].cancel()
    #         self.timer_record[timer] = None
    #         self.timer_record.pop(timer)

    # 使用asyncio+while循环实现定时器
    def set_interval(self, interval: int, fn, **fn_args):
        timer_record = self.__generate_record_key()

        def start_loop(loop):
            asyncio.set_event_loop(loop)
            loop.run_forever()

        async def _set_interval():
            while timer_record in self.timer_record:
                fn(**fn_args)
                await asyncio.sleep(interval)

        self.timer_record[timer_record] = f'interval-{timer_record}'

        event_loop = asyncio.new_event_loop()

        self.event_loop_record[timer_record] = threading.Thread(target=start_loop, args=(event_loop,), daemon=True)
        self.event_loop_record[timer_record].start()
        asyncio.run_coroutine_threadsafe(_set_interval(), event_loop)

        return timer_record

    def clear_interval(self, timer):
        print('clear_interval: ', timer)

        if self.timer_record[timer]:
            self.timer_record.pop(timer)

        if self.event_loop_record[timer]:
            self.event_loop_record.pop(timer)


def task(arg: str):
    print("task excute with arg: ", arg)


timer = Timer()
__tag = timer.set_interval(2, task, arg='aaaaa')

print('__tag', __tag)

threading.Timer(9, timer.clear_interval, (__tag,)).start()
