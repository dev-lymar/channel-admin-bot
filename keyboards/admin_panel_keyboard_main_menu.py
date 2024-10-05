from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def admin_panel_keyboard_main_menu() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text="Создать пост", callback_data="create_post"),
        types.InlineKeyboardButton(text="Удалить пост", callback_data="delete_post"),
    )

    return builder.as_markup()
