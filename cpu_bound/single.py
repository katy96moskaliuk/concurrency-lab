import time


def cpu_task():
    total = 0
    for i in range(50_000_000):
        total += i
    return total


start = time.time()

cpu_task()

end = time.time()

print("Time:", end - start)