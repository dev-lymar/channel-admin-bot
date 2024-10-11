from aiogram import F, Router, types
from aiogram.utils.i18n import gettext as _

from keyboards.admin_panel_keyboard_take_user_role import admin_panel_keyboard_take_user_role

router = Router()


@router.callback_query(F.data == "make_user_role")
async def admin_panel_create_user_role_callback(callback: types.CallbackQuery) -> None:
    """
    Handle callback for displaying user role selection options.

    Args:
        callback (types.CallbackQuery): The callback query object from the user interaction.
    """
    await callback.message.delete()

    await callback.message.answer(text=_("user_role.role_selection"),
                                  reply_markup=await admin_panel_keyboard_take_user_role())


def register_create_user_role_handlers(dp) -> None:
    dp.include_router(router)
