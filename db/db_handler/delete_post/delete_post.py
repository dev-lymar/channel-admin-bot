from sqlalchemy import delete

from db.models.models import Post, async_session


async def delete_post(post_id: int):
    """
    Delete a post by its ID.

    Args:
        post_id (int): The ID of the post to be deleted.

    """
    async with async_session() as session:
        await session.execute(delete(Post).where(Post.id == post_id))
        await session.commit()
