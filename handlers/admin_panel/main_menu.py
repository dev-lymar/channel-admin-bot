from aiogram import F, Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.user_role.check_user_role import check_db_user_role
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.content_manager_keyboard_main_menu import content_manager_panel_keyboard_main_menu

router = Router()


@router.callback_query(F.data == "main_menu", StateFilter("*"))
async def admin_panel_main_menu_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = int(callback.from_user.id)
    check_user_role = await check_db_user_role(user_id)
    curr_state = await state.get_state()

    if check_user_role == 'admin':
        if curr_state is None:
            await callback.message.answer(text=_("main_menu.welcome.message"),
                                          reply_markup=await admin_panel_keyboard_main_menu())
        elif curr_state is not None:
            await state.clear()
            await callback.message.delete()
            await callback.message.answer(text=_("main_menu.welcome.message"),
                                          reply_markup=await admin_panel_keyboard_main_menu())
    elif check_user_role == 'content_manager':
        if curr_state is None:
            await callback.message.answer(text=_("main_menu.welcome.message"),
                                          reply_markup=await content_manager_panel_keyboard_main_menu())
        elif curr_state is not None:
            await state.clear()
            await callback.message.delete()
            await callback.message.answer(text=_("main_menu.welcome.message"),
                                          reply_markup=await content_manager_panel_keyboard_main_menu())
    await callback.answer()


def register_main_menu_handlers(dp) -> None:
    dp.include_router(router)
