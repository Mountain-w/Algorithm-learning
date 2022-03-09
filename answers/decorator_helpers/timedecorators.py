import time


def time_helper(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(f'耗时：{(time.time() - start_time)}s')
    return inner
