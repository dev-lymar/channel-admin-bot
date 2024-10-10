from sqlalchemy import select

from db.models.models import Post, async_session


async def get_post_name(post_id: int):
    async with async_session() as session:
        result = await session.scalar(select(Post).where(Post.id == post_id))

        if result is None:
            return None
        else:
            return result
