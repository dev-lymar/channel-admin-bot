from db.models.models import Post, async_session


async def create_post(post_name: str, post_description: str, post_image: str, post_tag: str,
                      user_name: str, create_date: str, create_time: str):
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
