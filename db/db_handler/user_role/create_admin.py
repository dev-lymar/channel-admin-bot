from db.models.models import User, async_session


async def create_admin(user_id: int, user_name: str):
    """
    Create a new user with the 'admin' role.

    Args:
        user_id (int): The unique ID of the user.
        user_name (str): The name of the user.

    """
    async with async_session() as session:
        new_user = User(user_id=user_id, user_name=user_name, user_role="admin")
        session.add(new_user)
        await session.commit()
