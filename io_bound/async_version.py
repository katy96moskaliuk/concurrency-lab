import asyncio
import time


async def io_task():
    await asyncio.sleep(1)


async def main():
    tasks = [io_task() for _ in range(10)]
    await asyncio.gather(*tasks)


start = time.time()

asyncio.run(main())

end = time.time()

print("Async IO time:", end - start)