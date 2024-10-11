from db.models.models import User, async_session


async def create_content_manager(user_id: int, user_name: str):
    """
    Create a new user with the 'content_manager' role.

    Args:
        user_id (int): The unique ID of the user.
        user_name (str): The name of the user.

    """
    async with async_session() as session:
        new_user = User(user_id=user_id, user_name=user_name, user_role="content_manager")
        session.add(new_user)
        await session.commit()
