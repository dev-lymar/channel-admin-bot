from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.user_role.check_user_role import check_db_user_role
from db.db_handler.user_role.delete_user_role import delete_user_role
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.user_role_actions import Delete_role_from_user

router = Router()


@router.callback_query(F.data == "delete_user_role")
async def admin_panel_delete_user_role(callback: types.CallbackQuery, state=FSMContext) -> None:
    await state.set_state(Delete_role_from_user.user_id)

    await callback.message.delete()
    await callback.message.answer(text=_("user_role.delete.get_user_id"),
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Delete_role_from_user.user_id)
async def load_user_id(message: types.Message, state: FSMContext) -> None:
    try:
        check = await check_db_user_role(user_id=int(message.text))
        int_user_id = int(message.text)

        if check == "None":
            await state.clear()
            await message.answer(text=_("user_role.error.id_not_found").format(user_id=message.text),
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
        else:
            await delete_user_role(user_id=int_user_id)
            await message.answer(text=_("user_role.delete.successfully_deleted").format(user_id=int_user_id),
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
            await state.clear()

    except ValueError:
        await state.clear()
        await message.answer(text=_("user_role.error.value_error").format(user_id=message.text),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_delete_user_role_handlers(dp) -> None:
    dp.include_router(router)
