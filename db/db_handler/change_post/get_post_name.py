from sqlalchemy import select

from db.models.models import Post, async_session


async def get_post_name(post_id: int):
    """
    Retrieve the name of a post by its ID.

    Args:
        post_id (int): The ID of the post.

    Returns:
        str or None: The name of the post if found, otherwise None.
    """
    async with async_session() as session:
        result = await session.scalar(select(Post).where(Post.id == post_id))

        if result is None:
            return None
        else:
            return result
