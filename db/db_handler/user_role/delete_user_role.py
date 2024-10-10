from sqlalchemy import delete

from db.models.models import User, async_session


async def delete_user_role(user_id: int):
    async with async_session() as session:
        await session.execute(delete(User).where(User.user_id == user_id))
        await session.commit()
