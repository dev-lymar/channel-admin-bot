from db.models.models import Post, async_session


async def change_post(post_id: int, post_name: str, post_description: str, post_image: str, post_tag: str,
                      change_user_name: str, change_date: str, change_time: str):
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
