import aiohttp
import asyncio

#Reusing a Single Session

async def fetch_good(session, url, idx):
    async with session.get(url) as response:
        text = await response.text()
    
        print(f"Request {idx}: {response.status}")

        return text[:60]
    

async def main():
     urls = ["https://example.com"] * 10
     async with aiohttp.ClientSession() as session:
         results = await asyncio.gather(*[fetch_good(session,url,i) for i,url in enumerate(urls)])
         print(results)

asyncio.run(main())