from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.user_role.check_user_role import check_db_user_role
from db.db_handler.user_role.create_admin import create_admin
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.user_role_actions import Create_user_role_admin

router = Router()


@router.callback_query(F.data == "take_user_role_admin")
async def load_user_role_admin_callback(callback: types.CallbackQuery, state=FSMContext) -> None:
    await state.set_state(Create_user_role_admin.user_id)

    await callback.message.delete()
    await callback.message.answer(text=_("user_role.get_user_id"),
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_user_role_admin.user_id)
async def load_user_id(message: types.Message, state: FSMContext) -> None:
    try:
        check = await check_db_user_role(user_id=int(message.text))

        if check == "admin":
            await state.clear()
            await message.answer(text=_("user_role.error.user_exists_as_admin").format(user_id=message.text),
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())

        elif check == "content_manager":
            await state.clear()
            await message.answer(text=_("user_role.error.user_exists_as_context_manager").format(user_id=message.text),
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
        else:
            await state.update_data(user_id=message.text)
            data = await state.get_data()
            user_id = int(data.get('user_id'))
            if user_id < 0:
                await state.clear()
                await message.answer(text=_("user_role.error.negative_id").format(user_id=user_id),
                                     reply_markup=await admin_panel_keyboard_back_to_main_menu())
            else:
                await state.set_state(Create_user_role_admin.user_name)
                await message.answer(text=_("user_role.create.get_admin_username").format(user_id=user_id),
                                     reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except ValueError:
        await state.clear()
        await message.answer(text=_("user_role.error.value_error").format(user_id=message.text),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_user_role_admin.user_name)
async def load_user_name(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    int_data_user_id = int(data.get('user_id'))
    res = message.text.isdigit()

    if res:
        await state.clear()
        await message.answer(text=_("user_role.error.invalid_username").format(user_id=int_data_user_id),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())
    else:
        await state.update_data(user_name=message.text)
        await create_admin(user_id=int_data_user_id, user_name=message.text)
        await message.answer(text=_("user_role.create.admin_role_successfully_created").
                             format(user_id=int_data_user_id,
                                    user_username=message.text),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())
        await state.clear()


def register_load_user_role_admin_handlers(dp) -> None:
    dp.include_router(router)
