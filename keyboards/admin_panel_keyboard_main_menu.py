from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def admin_panel_keyboard_main_menu() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text="Создать пост", callback_data="create_post"))
    builder.row(types.InlineKeyboardButton(text="Редактировать пост", callback_data="change_post"))
    builder.row(types.InlineKeyboardButton(text="Удалить пост", callback_data="delete_post"))
    builder.row(types.InlineKeyboardButton(text="Опубликовать пост", callback_data="publish_post"),
                types.InlineKeyboardButton(text="Посмотреть пост", callback_data="check_post"))

    builder.row(types.InlineKeyboardButton(text="Назначить роль пользователю", callback_data="make_user_role"))
    builder.row(types.InlineKeyboardButton(text="Удалить роль у пользователю", callback_data="delete_user_role"))

    return builder.as_markup()
