from aiogram import types, Router, F
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu


router = Router()


@router.callback_query(F.data == "main_menu")
async def admin_panel_main_menu_callback(callback: types.CallbackQuery):
    await callback.message.delete()

    await callback.message.answer(text="Вы находитесь в главном меню",
                                  reply_markup=await admin_panel_keyboard_main_menu())


def register_main_menu_callback(dp) -> None:
    dp.include_router(router)
