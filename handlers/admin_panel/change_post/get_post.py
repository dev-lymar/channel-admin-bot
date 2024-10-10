import datetime

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.change_post.change_post import change_post
from db.db_handler.change_post.get_post_name import get_post_name
from db.db_handler.create_post.check_username import check_db_user_name
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.post_actions import Change_post

router = Router()


@router.callback_query(F.data == "change_post")
async def admin_panel_change_post_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Change_post.post_id)
    await callback.message.delete()

    await callback.message.answer(text=_("post.edit.enter_id"),
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Change_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    try:
        row = await get_post_name(int(message.text))
        await state.update_data(post_id=message.text)
        await state.set_state(Change_post.post_name)
        await message.answer(text=_("post.edit.new_title").format(post_id=message.text,
                                                                  post_title=row.post_name),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())
    except TypeError:
        await state.clear()
        await message.answer(text=_("post.error.id_not_found").format(post_id=message.text),
                             reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Change_post.post_name)
async def post_name(message: types.Message, state: FSMContext):
    await state.update_data(post_name=message.html_text)
    await state.set_state(Change_post.post_description)
    data = await state.get_data()
    data_post_id = data.get("post_id")
    data_post_name = data.get("post_name")
    await message.answer(text=_("post.edit.new_description").format(post_id=data_post_id,
                                                                    post_title=data_post_name),
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Change_post.post_description)
async def post_description(message: types.Message, state: FSMContext):
    await state.update_data(post_description=message.html_text)
    await state.set_state(Change_post.post_tag)
    data = await state.get_data()
    data_post_id = data.get("post_id")
    data_post_name = data.get("post_name")
    data_post_description = data.get("post_description")
    await message.answer(text=_("post.edit.new_tag").format(post_id=data_post_id,
                                                            post_name=data_post_name,
                                                            post_description=data_post_description),
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Change_post.post_tag)
async def post_tag(message: types.Message, state: FSMContext):
    await state.update_data(post_tag=message.text)
    await state.set_state(Change_post.post_image)
    data = await state.get_data()
    data_post_id = data.get("post_id")
    data_post_name = data.get("post_name")
    data_post_description = data.get("post_description")
    data_post_tag = data.get("post_tag")
    await message.answer(text=_("post.edit.new_image").format(post_id=data_post_id,
                                                              post_name=data_post_name,
                                                              post_description=data_post_description,
                                                              post_tag=data_post_tag),
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Change_post.post_image)
async def post_image(message: types.Message, state: FSMContext):
    await state.update_data(post_image=message.photo[0].file_id)
    data = await state.get_data()

    user_id = int(message.from_user.id)
    data_post_id = int(data.get("post_id"))
    new_post_name = str(data.get("post_name"))
    new_post_description = str(data.get("post_description"))
    new_post_image = str(data.get("post_image"))
    new_post_tag = str(data.get("post_tag"))
    current_time = datetime.datetime.now()
    change_date = str(current_time.date())
    change_time = str(current_time.time().replace(microsecond=0))
    change_user_name = await check_db_user_name(user_id=user_id)

    await change_post(post_id=data_post_id,
                      post_name=new_post_name,
                      post_description=new_post_description,
                      post_image=new_post_image,
                      post_tag=new_post_tag,
                      change_user_name=change_user_name,
                      change_date=change_date,
                      change_time=change_time
                      )
    await message.answer_photo(photo=new_post_image,
                               caption=_("post.edit.successfully_edited_info").
                               format(post_name=new_post_name,
                                      post_description=new_post_description,
                                      post_tag=new_post_tag,
                                      change_user_name=change_user_name,
                                      change_date=change_date,
                                      change_time=change_time,),
                               reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_change_post_handlers(dp) -> None:
    dp.include_router(router)
