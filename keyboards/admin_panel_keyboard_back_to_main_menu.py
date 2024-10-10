from aiogram import types
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def admin_panel_keyboard_back_to_main_menu() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text=_("kb.back_to_main_menu"), callback_data="main_menu"),

    )

    return builder.as_markup()
