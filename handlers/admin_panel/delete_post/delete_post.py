from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.change_post.get_post_name import get_post_name
from db.db_handler.delete_post.delete_post import delete_post
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.post_actions import Delete_post

router = Router()


@router.callback_query(F.data == "delete_post")
async def admin_panel_delete_post_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    """
    Handle callback for initiating the process of deleting a post.

    Args:
        callback (types.CallbackQuery): The callback query object from the user interaction.
        state (FSMContext): The FSM context for managing the state of the deletion process.
    """
    await state.set_state(Delete_post.post_id)
    await callback.message.delete()

    await callback.message.answer(text=_("post.get_from_user.post_id"),
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Delete_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    """
    Handle input of post ID for deleting a post.

    Args:
        message (types.Message): The message containing the post ID from the user.
        state (FSMContext): The FSM context for managing the state of the deletion process.
    """
    try:
        row = await get_post_name(int(message.text))
        await state.update_data(post_id=message.text)
        data = await state.get_data()
        int_post_id = int(data.get("post_id"))
        await delete_post(post_id=int_post_id)
        await state.clear()
        await message.answer(text=_("post.delete.successfully_deleted").format(post_id=message.text,
                                                                               post_name=row.post_name),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except TypeError:
        await state.clear()
        await message.answer(text=_("post.error.id_not_found").format(post_id=message.text),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_delete_post_handlers(dp) -> None:
    dp.include_router(router)
