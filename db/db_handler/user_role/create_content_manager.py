from db.models.models import User, async_session


async def create_content_manager(user_id: int, username: str):
    async with async_session() as session:
        new_user = User(user_id=user_id, user_name=username, user_role="content_manager")
        session.add(new_user)
        await session.commit()
