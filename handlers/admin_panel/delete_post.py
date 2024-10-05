from aiogram import types, Router, F
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


router = Router()


@router.callback_query(F.data == "delete_post")
async def admin_panel_delete_post_callback(callback: types.CallbackQuery) -> None:
    await callback.message.delete()

    await callback.message.answer(text="Можно будет удалить пост",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_delete_post_callback(dp) -> None:
    dp.include_router(router)
