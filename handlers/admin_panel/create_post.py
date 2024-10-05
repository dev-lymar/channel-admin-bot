from aiogram import types, Router, F
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


router = Router()


@router.callback_query(F.data == "create_post")
async def admin_panel_create_post_callback(callback: types.CallbackQuery) -> None:
    await callback.message.delete()

    await callback.message.answer(text="Можно будет создавать пост",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_create_post_callback(dp) -> None:
    dp.include_router(router)
