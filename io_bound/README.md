# Concurrency Lab (Python)

This project is a small experimental lab to understand how concurrency works in Python.

It compares different execution models:

- CPU-bound tasks
- I/O-bound tasks
- Threads
- Processes (multiprocessing)
- Asyncio

---

#  What I learned

## 1. CPU-bound tasks
CPU-heavy tasks (loops, calculations) are limited by Python's GIL.

- single process → baseline
- threads → no real speedup (GIL limitation)
- processes → real parallelism (uses multiple CPU cores)

---

## 2. I/O-bound tasks
I/O tasks spend time waiting (sleep, network, files).

- single → slow (sequential waiting)
- threads → faster (waiting overlaps)
- async → fastest (non-blocking event loop)

---

#  Concepts Covered

- Python GIL (Global Interpreter Lock)
- multiprocessing
- threading
- asyncio / event loop
- CPU-bound vs I/O-bound distinction

---

#  Project Structure
cpu_bound/
single.py
threads.py
processes.py

io_bound/
single.py
threads.py
async_version.py

benchmarks/
timer.py


---

#  Example Results (approx)

## CPU-bound
- single: ~1.4s
- threads: ~5s (no improvement)
- processes: ~0.4s (real parallelism)

## I/O-bound
- single: ~10s
- threads: ~1s
- async: ~1s

---

#  Key Takeaways

- Threads do NOT improve CPU performance in Python
- Processes bypass GIL and enable real parallelism
- Async is best for high-latency I/O tasks
- Choosing the right model depends on the task type

---

#  Purpose

This project was built for learning purposes to understand:
how Python handles concurrency internally.

---

#  Author

Junior developer learning backend and system fundamentals.