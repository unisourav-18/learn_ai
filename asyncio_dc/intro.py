import asyncio
import time

async def greet_after_delay(name):
    print(f"starting {name}...")
    await asyncio.sleep(2)
    print(f"hello {name}")

# async def main():
#     start = time.perf_counter()

#     await greet_after_delay("Alice")
#     await greet_after_delay("Bob")
#     await greet_after_delay("Charlie")

#     elapsed = time.perf_counter() - start
#     print(f"total time: {elapsed:.2f} seconds")

# asyncio.run(main())

# above code is sequential async not useful at all 

# async def main():
#     start = time.perf_counter()

#     await asyncio.gather(
#         greet_after_delay("Alice"),
#         greet_after_delay("Bob"),
#         greet_after_delay("Charlie"),
#     )

#     elapsed = time.perf_counter() - start
#     print(f"total time: {elapsed:.2f} seconds")

# asyncio.run(main())

# above code is the example of running concurrent tasks

async def fetch_number(n):
    await asyncio.sleep(1)
    return n * 10

async def main():
    results = await asyncio.gather(
        fetch_number(1),
        fetch_number(2),
        fetch_number(3),
    )
    print(results)
    print(type(results))  #list type

asyncio.run(main())

# we can also store and return values using asyncio.gather()