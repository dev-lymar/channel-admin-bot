from db.models.models import User, async_session


async def create_admin(user_id: int, user_name: str):
    async with async_session() as session:
        new_user = User(user_id=user_id, user_name=user_name, user_role="admin")
        session.add(new_user)
        await session.commit()
