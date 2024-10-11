from sqlalchemy import select

from db.models.models import Post, async_session


async def get_post(post_id: int):
    """
    Retrieve detailed information about a specific post by its ID.

    Args:
        post_id (int): The ID of the post to retrieve.

    Returns:
        tuple or None: A tuple containing the post's name, description, image, and tag if found,
                       otherwise None.
    """
    async with async_session() as session:
        result = await session.execute(
            select(Post.post_name, Post.post_description, Post.post_image, Post.post_tag).where(Post.id == post_id))
        row = result.fetchone()

        if row is None:
            return None
        else:
            return row
