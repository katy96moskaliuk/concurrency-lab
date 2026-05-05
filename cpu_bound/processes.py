from multiprocessing import Process
import time

def cpu_task():
	total = 0
	for i in range(50_000_000):
		total += i

if __name__ == '__main__':

	processes = []

	start = time.time()

	for _ in range(4):
		p = Process(target=cpu_task)
		processes.append(p)
		p.start()

	print(processes)

	for p in processes:
		p.join()

	end = time.time()

	print("Processes time:", end - start)

		