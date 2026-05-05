import time


def measure(func, *args, **kwargs):
    start = time.time()

    result = func(*args, **kwargs)

    end = time.time()

    return end - start, result