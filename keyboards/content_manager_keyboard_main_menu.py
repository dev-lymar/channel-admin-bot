from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def content_manager_panel_keyboard_main_menu() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="Создать пост", callback_data="create_post"))
    builder.row(types.InlineKeyboardButton(text="Редактировать пост", callback_data="change_post"))
    builder.row(types.InlineKeyboardButton(text="Удалить пост", callback_data="delete_post"))
    builder.row(types.InlineKeyboardButton(text="Опубликовать пост", callback_data="publish_post"),
                types.InlineKeyboardButton(text="Посмотреть пост", callback_data="check_post"))

    return builder.as_markup()
