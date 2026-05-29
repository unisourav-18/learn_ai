#Async HTTP request example: Scraping Hacker News


import aiohttp
import asyncio

HN_API = "https://hacker-news.firebaseio.com/v0"

async def main():
    async with aiohttp.ClientSession() as session:
        # Get top story IDs
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()
        
        print(f"Found {len(story_ids)} stories")
        print(f"First 5 IDs: {story_ids[:5]}")
        
        # Fetch first story details
        first_id = story_ids[0]
        async with session.get(f"{HN_API}/item/{first_id}.json") as response:
            story = await response.json()
        
        print(f"\nStory structure:")
        for key, value in story.items():
            print(f"  {key}: {repr(value)[:50]}")

asyncio.run(main())