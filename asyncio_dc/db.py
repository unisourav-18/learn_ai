import aiosqlite
import asyncio
import aiohttp


async def init_db(db_path):
    async with aiosqlite.connect(db_path) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY,
                title TEXT,
                url TEXT,
                score INTEGER,
                fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()

asyncio.run(init_db("stories.db"))


async def save_story(db, story):
    await db.execute(
        "INSERT OR REPLACE INTO stories (id, title, url, score) VALUES (?, ?, ?, ?)",
        (story["id"], story.get("title", ""), story.get("url", ""), story.get("score", 0))
    )