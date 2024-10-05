from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from states.create_user_role import Create_user_role_content_manager
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

router = Router()


@router.callback_query(F.data == "take_user_role_content_manager")
async def load_user_role_content_manager_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Create_user_role_content_manager.user_id)

    await callback.message.delete()
    await callback.message.answer(text="Роль успешно выбрана. \nПришлите ID пользователя, которого хотите добавить",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_user_role_content_manager.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    await state.update_data(user_id=message.text)
    data = await state.get_data()
    user_id = data.get('user_id')

    await state.clear()
    await message.delete()
    await message.answer(f"Контент менеджер с ID {user_id} успешно добавлен!",
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_load_user_role_content_manager_callback(dp) -> None:
    dp.include_router(router)
