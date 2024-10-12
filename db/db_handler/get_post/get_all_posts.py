from sqlalchemy import select

from db.models.models import Post, async_session


async def get_posts() -> list:
    """
    Retrieve a list of all posts with their ID, name, and tag.

    Returns:
        list: A list of tuples, each containing the ID, name, and tag of a post.
              Returns an empty list if no posts are found.
    """
    async with async_session() as session:
        result = await session.execute(
            select(Post.id, Post.post_name, Post.post_tag))
        rows = result.all()

        return rows if rows else []
