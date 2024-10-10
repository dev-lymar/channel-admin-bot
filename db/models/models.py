from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config.bot_config import DB_URL

engine = create_async_engine(DB_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    user_role: Mapped[str] = mapped_column()
    user_name: Mapped[str] = mapped_column()


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    post_name: Mapped[str] = mapped_column()
    post_description: Mapped[str] = mapped_column()
    post_image: Mapped[str] = mapped_column()
    post_tag: Mapped[str] = mapped_column()
    user_name: Mapped[str] = mapped_column()
    create_date: Mapped[str] = mapped_column()
    create_time: Mapped[str] = mapped_column()
    change_user_name: Mapped[str] = mapped_column()
    change_date: Mapped[str] = mapped_column()
    change_time: Mapped[str] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
