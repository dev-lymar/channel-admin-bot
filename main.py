import asyncio

from handlers import register_routers
from config.bot_config import bot, dp
from db.models.models import async_main


async def main() -> None:
    await async_main()
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
