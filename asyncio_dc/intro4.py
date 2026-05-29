#fetching 10 stories sequentially

import aiohttp
import asyncio
import time

HN_API = "https://hacker-news.firebaseio.com/v0"

async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f"{HN_API}/topstories.json") as response:
#             story_ids = await response.json()
        
#         start = time.perf_counter()
#         stories = []
#         for story_id in story_ids[:10]:
#             story = await fetch_story(session, story_id)
#             stories.append(story)
#         elapsed = time.perf_counter() - start
        
#         print(f"Sequential: Fetched {len(stories)} stories in {elapsed:.2f} seconds")

# asyncio.run(main())

async def main():  #fetching 10 stories concurrently
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()
        
        start = time.perf_counter()
        tasks = [fetch_story(session, story_id) for story_id in story_ids[:10]]
        stories = await asyncio.gather(*tasks)
        elapsed = time.perf_counter() - start
        
        print(f"Concurrent: Fetched {len(stories)} stories in {elapsed:.2f} seconds")
        print("\nTop 3 stories:")
        for story in stories[:3]:
            print(f"  - {story.get('title', 'No title')}")

asyncio.run(main())

