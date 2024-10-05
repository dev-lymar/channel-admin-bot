from aiogram import types, Router
from aiogram.filters import CommandStart
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from db.db_handler.user_role.check_user_role import check_db_user_role


router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    user_id = int(message.from_user.id)
    check_user_role = await check_db_user_role(user_id=user_id)

    if check_user_role == 'admin':
        await message.answer(text="Вы вошли как админ",
                             reply_markup=await admin_panel_keyboard_main_menu())
    else:
        await message.answer("Вы не админ!")


def register_start_command(dp) -> None:
    dp.include_router(router)
