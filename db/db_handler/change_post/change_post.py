from db.models.models import Post, async_session


async def change_post(post_id: int, post_name: str, post_description: str, post_image: str, post_tag: str,
                      change_user_name: str, change_date: str, change_time: str):
    """
    Update an existing post with new details.

    Args:
        post_id (int): The ID of the post to be updated.
        post_name (str): The new name of the post.
        post_description (str): The new description of the post.
        post_image (str): The new image URL or path for the post.
        post_tag (str): The new tag associated with the post.
        change_user_name (str): The name of the user making the change.
        change_date (str): The date of the change in 'YYYY-MM-DD' format.
        change_time (str): The time of the change in 'HH:MM:SS' format.

    """
    async with async_session() as session:
        existing_post = await session.get(Post, post_id)
        existing_post.post_name = post_name
        existing_post.post_description = post_description
        existing_post.post_tag = post_tag
        existing_post.post_image = post_image
        existing_post.change_user_name = change_user_name
        existing_post.change_date = change_date
        existing_post.change_time = change_time
        await session.commit()
