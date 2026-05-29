import asyncio
import time

async def slow_operation():
    print("Starting slow operation...")
    await asyncio.sleep(5)
    return "Done"



async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(f"Success: {result}")
    except asyncio.TimeoutError:
        print("Operation timed out after 2 seconds")



asyncio.run(main())