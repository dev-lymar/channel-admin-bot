from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from db.db_handler.change_post.get_post_name import get_post_name
from db.db_handler.delete_post.delete_post import delete_post
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.post_actions import Delete_post

router = Router()


@router.callback_query(F.data == "delete_post")
async def admin_panel_delete_post_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Delete_post.post_id)
    await callback.message.delete()

    await callback.message.answer(text="Укажите ID поста который надо удалить:",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Delete_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    try:
        row = await get_post_name(int(message.text))
        await state.update_data(post_id=message.text)
        data = await state.get_data()
        int_post_id = int(data.get("post_id"))
        await delete_post(post_id=int_post_id)
        await state.clear()
        await message.answer(text=f"ID поста: {message.text}\n"
                                  f"Название поста: {row.post_name}\n\n"
                                  "Пост удален",
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except TypeError:
        await state.clear()
        await message.answer(text=f"ID поста: {message.text}\n"
                                  f"Ошибка. Поста с таким ID нет в базе данных!\n"
                                  "Попробуйте еще раз.",
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_delete_post_handlers(dp) -> None:
    dp.include_router(router)
