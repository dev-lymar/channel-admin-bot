from aiogram import types
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def admin_panel_keyboard_take_user_role() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text=_("kb.select_admin_role"), callback_data="take_user_role_admin"),
        types.InlineKeyboardButton(text=_("kb.select_context_manager_role"),
                                   callback_data="take_user_role_content_manager"),
    )

    return builder.as_markup()
