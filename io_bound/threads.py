import time
import threading

def io_task():
	time.sleep(1)

threads = []

start = time.time()

for _ in range(10):
	t = threading.Thread(target=io_task)
	threads.append(t)
	t.start()

for t in threads:
	t.join()

end = time.time()

print("Threads IO time:", end - start)