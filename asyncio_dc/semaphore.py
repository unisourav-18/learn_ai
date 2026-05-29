#Semaphores are used for rate limiting
import aiohttp
import asyncio
import time

HN_API = "https://hacker-news.firebaseio.com/v0"



async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

async def fetch_story_limited(session, story_id, semaphore):
    async with semaphore:  # Acquire permit (or wait if none available)
        async with session.get(f"{HN_API}/item/{story_id}.json") as response:
            return await response.json()
    # Permit automatically released here


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = (await response.json())[:30]

        # Without rate limiting: all 30 at once
        start = time.perf_counter()
        await asyncio.gather(*[fetch_story(session, sid) for sid in story_ids])
        print(f"No limit: {time.perf_counter() - start:.2f}s (30 concurrent)")

        # With Semaphore(5): max 5 at a time
        semaphore = asyncio.Semaphore(5)
        start = time.perf_counter()
        await asyncio.gather(*[fetch_story_limited(session, sid, semaphore) for sid in story_ids])
        print(f"Semaphore(5): {time.perf_counter() - start:.2f}s (5 concurrent)")

asyncio.run(main())