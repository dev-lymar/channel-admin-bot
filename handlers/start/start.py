from aiogram import types, Router, F
from aiogram.filters import Command, CommandStart
from config.bot_config import dp, ADMIN
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu


router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message):
    user_id = str(message.from_user.id)

    if user_id == ADMIN:
        await message.answer(text="Вы вошли как админ",
                             reply_markup=await admin_panel_keyboard_main_menu())
    else:
        await message.answer("Вы не админ!")


def register_start_command(dp) -> None:
    dp.include_router(router)
