from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from config.bot_config import CHAT_ID, bot
from db.db_handler.get_post.get_post import get_post
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.post_actions import Publish_post

router = Router()


@router.callback_query(F.data == "publish_post")
async def admin_panel_publish_post_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Publish_post.post_id)
    await callback.message.delete()

    await callback.message.answer(text="Укажите ID поста:",
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Publish_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    try:
        row = await get_post(int(message.text))
        post_name, post_description, post_image = row
        await state.clear()

        await bot.send_photo(chat_id=CHAT_ID,
                             photo=post_image,
                             caption=f"{post_name}\n\n"
                                     f"{post_description}")
        await message.answer_photo(photo=row.post_image,
                                   caption=f"ID поста: {message.text}\n"
                                           f"Название поста: {post_name}\n\n"
                                           f"Описание поста: {post_description}\n\n"
                                           "Пост опубликован!",
                                   reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except TypeError:
        await state.clear()
        await message.answer(text=f"ID поста: {message.text}\n"
                                  f"Ошибка. Поста с таким ID нет в базе данных!\n"
                                  "Попробуйте еще раз.",
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_publish_post_handlers(dp) -> None:
    dp.include_router(router)
