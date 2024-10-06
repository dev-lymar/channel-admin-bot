from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import dotenv_values
import logging

config = dotenv_values("./config/.env")
API_TOKEN = config["API_TOKEN"]
ADMIN = config["ADMIN_ID"]
DB_URL = config["DB_URL"]
CHAT_ID = config["CHAT_ID"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
