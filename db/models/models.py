from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config.bot_config import DB_URL

engine = create_async_engine(DB_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    """
    Represents a user in the database.

    Attributes:
        id (int): The primary key of the user.
        user_id (BigInteger): The unique identifier of the user, usually matching their ID in the external system.
        user_role (str): The role of the user, such as 'admin' or 'content_manager'.
        user_name (str): The name of the user.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    user_role: Mapped[str] = mapped_column()
    user_name: Mapped[str] = mapped_column()


class Post(Base):
    """
    Represents a post in the database.

    Attributes:
        id (int): The primary key of the post.
        post_name (str): The name/title of the post.
        post_description (str): A detailed description of the post.
        post_image (str): The URL or path to the image associated with the post.
        post_tag (str): A tag categorizing the post.
        user_name (str): The name of the user who created the post.
        create_date (str): The date when the post was created, in 'YYYY-MM-DD' format.
        create_time (str): The time when the post was created, in 'HH:MM:SS' format.
        change_user_name (str): The name of the user who last modified the post.
        change_date (str): The date when the post was last modified, in 'YYYY-MM-DD' format.
        change_time (str): The time when the post was last modified, in 'HH:MM:SS' format.
    """
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
    """
    Initialize the database by creating all tables defined in the models.

    This function establishes an asynchronous connection to the database and
    creates all tables defined in the Base metadata. It should be run once
    during the setup or migration process to ensure that the database schema
    is in sync with the models.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
