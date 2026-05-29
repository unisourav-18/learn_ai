import aiohttp
import aiosqlite
import asyncio

HN_API = "https://hacker-news.firebaseio.com/v0"

async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

async def fetch_story_limited(session, story_id, semaphore):
    async with semaphore:
        story = await fetch_story(session, story_id)
        if story:
            return story
        return None

async def save_story(db, story):
    await db.execute(
        "INSERT OR REPLACE INTO stories (id, title, url, score) VALUES (?, ?, ?, ?)",
        (story["id"], story.get("title", ""), story.get("url", ""), story.get("score", 0))
    )

async def main():
    # Initialize database
    async with aiosqlite.connect("hn_stories.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY,
                title TEXT,
                url TEXT,
                score INTEGER,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Fetch stories
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{HN_API}/topstories.json") as response:
                story_ids = await response.json()
            
            semaphore = asyncio.Semaphore(5)
            tasks = [fetch_story_limited(session, sid, semaphore) for sid in story_ids[:20]]
            stories = await asyncio.gather(*tasks)
        
        # Save to database
        for story in stories:
            if story:
                await save_story(db, story)
        await db.commit()
        
        # Query and display
        cursor = await db.execute("SELECT id, title, score FROM stories ORDER BY score DESC LIMIT 5")
        rows = await cursor.fetchall()
        
        print(f"Saved {len([s for s in stories if s])} stories. Top 5 by score:")
        for row in rows:
            print(f"  [{row[2]}] {row[1][:50]}")

asyncio.run(main())