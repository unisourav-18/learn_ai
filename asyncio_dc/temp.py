import asyncio

async def get_message():
    await asyncio.sleep(1)
    return "Hello!"

async def main():
    message = await get_message()  
    print(message)

asyncio.run(main())