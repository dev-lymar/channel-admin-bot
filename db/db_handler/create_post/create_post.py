from db.models.models import Post, async_session


async def create_post(post_name: str, post_description: str, post_image: str, post_tag: str,
                      user_name: str, create_date: str, create_time: str):
    """
    Create a new post in the database.

    Args:
        post_name (str): The name of the post.
        post_description (str): A description of the post.
        post_image (str): The image URL or path for the post.
        post_tag (str): A tag associated with the post.
        user_name (str): The name of the user creating the post.
        create_date (str): The creation date in 'YYYY-MM-DD' format.
        create_time (str): The creation time in 'HH:MM:SS' format.
    """
    async with async_session() as session:
        new_post = Post(post_name=post_name,
                        post_description=post_description,
                        post_image=post_image,
                        post_tag=post_tag,
                        user_name=user_name,
                        create_date=create_date,
                        create_time=create_time
                        )
        session.add(new_post)
        await session.commit()
