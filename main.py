import asyncio

from handlers import register_routers
from config.bot_config import bot, dp


async def main() -> None:
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
