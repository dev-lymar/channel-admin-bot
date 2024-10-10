from aiogram import types
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def admin_panel_keyboard_main_menu() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(text=_("kb.post.create"), callback_data="create_post"))
    builder.row(types.InlineKeyboardButton(text=_("kb.post.edit"), callback_data="change_post"))
    builder.row(types.InlineKeyboardButton(text=_("kb.post.delete"), callback_data="delete_post"))
    builder.row(types.InlineKeyboardButton(text=_("kb.post.publish"), callback_data="publish_post"),
                types.InlineKeyboardButton(text=_("kb.post.check"), callback_data="check_post"))

    builder.row(types.InlineKeyboardButton(text=_("kb.user_role.create"), callback_data="make_user_role"))
    builder.row(types.InlineKeyboardButton(text=_("kb.user_role.delete"), callback_data="delete_user_role"))

    return builder.as_markup()
