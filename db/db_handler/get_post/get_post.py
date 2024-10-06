from sqlalchemy import select

from db.models.models import Post, async_session


async def get_post(post_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(Post.post_name, Post.post_description, Post.post_image).where(Post.id == post_id))
        row = result.fetchone()

        if row is None:
            return None
        else:
            return row
