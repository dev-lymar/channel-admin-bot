from aiogram import types, Router, F
from keyboards.admin_panel_keyboard_take_user_role import admin_panel_keyboard_take_user_role


router = Router()


@router.callback_query(F.data == "make_user_role")
async def admin_panel_create_user_role_callback(callback: types.CallbackQuery) -> None:
    await callback.message.delete()

    await callback.message.answer(text="Кого Вы хотите добавить ?",
                                  reply_markup=await admin_panel_keyboard_take_user_role())


def register_create_user_role_callback(dp) -> None:
    dp.include_router(router)
