from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu


router = Router()


@router.callback_query(F.data == "main_menu", StateFilter("*"))
async def admin_panel_main_menu_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    curr_state = await state.get_state()

    if curr_state is None:
        await callback.message.answer(text="Вы находитесь в главном меню",
                                      reply_markup=await admin_panel_keyboard_main_menu())
    elif curr_state is not None:
        await state.clear()
        await callback.message.delete()
        await callback.message.answer(text="Вы находитесь в главном меню",
                                      reply_markup=await admin_panel_keyboard_main_menu())
    await callback.answer()


def register_main_menu_handlers(dp) -> None:
    dp.include_router(router)
