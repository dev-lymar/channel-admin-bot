import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.i18n import I18n
from dotenv import dotenv_values

config = dotenv_values("./config/.env")
API_TOKEN = config["API_TOKEN"]
ADMIN = config["ADMIN_ID"]
DB_URL = config["DB_URL"]
CHAT_ID = config["CHAT_ID"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

i18 = I18n(path='locales', default_locale='en', domain='messages')
