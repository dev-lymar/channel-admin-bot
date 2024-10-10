from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.get_post.get_post import get_post
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.post_actions import Check_post

router = Router()


@router.callback_query(F.data == "check_post")
async def admin_panel_check_post_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Check_post.post_id)
    await callback.message.delete()

    await callback.message.answer(text=_("post.get_from_user.post_id"),
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Check_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    try:
        row = await get_post(int(message.text))
        post_name, post_description, post_image, post_tag = row
        await state.clear()

        await message.answer_photo(photo=row.post_image,
                                   caption=_("post.check.post_content").format(post_id=message.text,
                                                                               post_name=post_name,
                                                                               post_description=post_description,
                                                                               post_tag=post_tag),
                                   reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except TypeError:
        await state.clear()
        await message.answer(text=_("post.error.id_not_found").format(post_id=message.text),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_check_post_handlers(dp) -> None:
    dp.include_router(router)
