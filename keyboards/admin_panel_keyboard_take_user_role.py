from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def admin_panel_keyboard_take_user_role() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(text="Администратор", callback_data="take_user_role_admin"),
        types.InlineKeyboardButton(text="Контент менеджер", callback_data="take_user_role_content_manager"),
    )

    return builder.as_markup()
