from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext as _

from config.bot_config import ADMIN
from db.db_handler.user_role.check_user_role import check_db_user_role
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.content_manager_keyboard_main_menu import content_manager_panel_keyboard_main_menu

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message) -> None:
    user_id = int(message.from_user.id)
    check_user_role = await check_db_user_role(user_id=user_id)

    if check_user_role == 'admin' or user_id == ADMIN:
        await message.answer(text=_("start.admin.message"),
                             reply_markup=await admin_panel_keyboard_main_menu())
    elif check_user_role == 'content_manager':
        await message.answer(text=_("start.context_manager.message"),
                             reply_markup=await content_manager_panel_keyboard_main_menu())
    else:
        await message.answer(_("start.denied_access.message"))


def register_start_command(dp) -> None:
    dp.include_router(router)
