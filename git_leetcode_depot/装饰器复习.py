# 此处为装饰器复习
import time


def func_inner(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        time.sleep(2)
        func(*args, **kwargs)
        stop_time = time.time()
        return '所用时间：{}'.format(stop_time - start_time)

    return inner


@func_inner
def ad_a_b(x, y):
    return x + y


print(ad_a_b(1, 6))
