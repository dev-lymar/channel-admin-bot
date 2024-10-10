from sqlalchemy import select

from db.models.models import User, async_session


async def check_db_user_role(user_id: int):
    async with async_session() as session:
        result = await session.scalar(select(User.user_role).where(User.user_id == user_id))

        if result is None:
            return None
        else:
            return result
