import time

def io_task():
	time.sleep(1)

start = time.time()

for _ in range(10):
	io_task()

end = time.time()

print("Single IO time:", end - start)