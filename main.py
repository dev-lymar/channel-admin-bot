import asyncio

from aiogram.utils.i18n.middleware import SimpleI18nMiddleware

from config.bot_config import bot, dp, i18
from db.models.models import async_main
from handlers import register_routers


async def main() -> None:
    await async_main()
    dp.update.middleware(SimpleI18nMiddleware(i18n=i18))
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
