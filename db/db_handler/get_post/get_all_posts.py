from sqlalchemy import select

from db.models.models import Post, async_session


async def get_posts() -> list:
    async with async_session() as session:
        result = await session.execute(
            select(Post.id, Post.post_name, Post.post_tag))
        rows = result.all()

        return rows if rows else []
