from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from states.user_role_actions import Delete_role_from_user
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from db.db_handler.user_role.delete_user_role import delete_user_role
from db.db_handler.user_role.check_user_role import check_db_user_role

router = Router()


@router.callback_query(F.data == "delete_user_role")
async def admin_panel_delete_user_role(callback: types.CallbackQuery, state=FSMContext) -> None:
    await state.set_state(Delete_role_from_user.user_id)

    await callback.message.delete()
    await callback.message.answer(text="Кого вы хотите удалить ?\nПришлите ID пользователя",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Delete_role_from_user.user_id)
async def load_user_id(message: types.Message, state: FSMContext) -> None:
    try:
        check = await check_db_user_role(user_id=int(message.text))
        int_user_id = int(message.text)

        if check == "None":
            await state.clear()
            await message.answer(f"Пользователя с таким ID нет в базе данных!\n"
                                 f"ID пользователя: {message.text}\n"
                                 f"Попробуйте еще раз.\n",
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
        else:
            await delete_user_role(user_id=int_user_id)
            await message.answer(f"Пользователь удален\n"
                                 f"ID пользователя: {int_user_id}\n",
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
            await state.clear()

    except ValueError:
        await state.clear()
        await message.answer(f"ID пользователя должно содержать только цифры!\n"
                             f"Вы ввели следующий ID: {message.text}\n"
                             f"Попробуйте еще раз.\n",
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_delete_user_role_handlers(dp) -> None:
    dp.include_router(router)
