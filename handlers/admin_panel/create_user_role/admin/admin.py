from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from states.create_user_role import Create_user_role_admin
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

router = Router()


@router.callback_query(F.data == "take_user_role_admin")
async def load_user_role_admin_callback(callback: types.CallbackQuery, state=FSMContext) -> None:
    await state.set_state(Create_user_role_admin.user_id)

    await callback.message.delete()
    await callback.message.answer(text="Роль успешно выбрана. \nПришлите ID пользователя, которого хотите добавить",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_user_role_admin.user_id)
async def load_user_id(message: types.Message, state: FSMContext) -> None:
    await state.update_data(user_id=message.text)
    data = await state.get_data()
    user_id = data.get('user_id')

    try:
        int_user_id = int(user_id)

        if int_user_id < 0:
            await state.clear()
            await message.answer(f"ID пользователя не может быть отрицательным!\n"
                                 f"Вы ввели следующий ID: {user_id}"
                                 f"Попробуйте еще раз.",
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
        else:
            await state.clear()
            await message.answer(f"Администратор с ID {user_id} успешно добавлен!",
                                 reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except ValueError:
        await state.clear()
        await message.answer(f"ID пользователя должно содержать только цифры!\n"
                             f"Вы ввели следующий ID: {user_id}"
                             f"Попробуйте еще раз.",
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_load_user_role_admin_callback(dp) -> None:
    dp.include_router(router)
