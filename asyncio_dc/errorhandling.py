#Error handling with asyncio.gather()

import asyncio
import time
import aiohttp

HN_API = "https://hacker-news.firebaseio.com/v0"

async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

async def fetch_story_strict(session, story_id):
    story = await fetch_story(session, story_id)
    if story is None:
        raise ValueError(f"Story not found: {story_id}")
    return story

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()

        ids_to_fetch = story_ids[:4] + [99999999999]

        results = await asyncio.gather(
            *[fetch_story_strict(session, sid) for sid in ids_to_fetch],
            return_exceptions=True  # Don't raise, return exceptions in list
        )

        # Separate successes from failures using isinstance()
        stories = [r for r in results if not isinstance(r, Exception)]
        errors = [r for r in results if isinstance(r, Exception)]

        print(f"Got {len(stories)} stories, {len(errors)} failed")

asyncio.run(main())