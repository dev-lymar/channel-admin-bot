import datetime

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from db.db_handler.create_post.check_username import check_db_user_name
from db.db_handler.create_post.create_post import create_post
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from states.post_actions import Create_post

router = Router()


@router.callback_query(F.data == "create_post")
async def admin_panel_create_post_callback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Create_post.post_name)
    await callback.message.delete()

    await callback.message.answer(text=_("post.create.title"),
                                  reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_post.post_name)
async def post_name(message: types.Message, state: FSMContext):
    await state.update_data(post_name=message.html_text)
    await state.set_state(Create_post.post_description)
    await message.answer(text=_("post.create.description").format(post_title=message.html_text),
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_post.post_description)
async def post_description(message: types.Message, state: FSMContext):
    await state.update_data(post_description=message.html_text)
    await state.set_state(Create_post.post_image)
    data = await state.get_data()
    data_post_name = data.get("post_name")
    data_post_description = data.get("post_description")
    await message.answer(text=_("post.create.image").format(post_title=data_post_name,
                                                            post_description=data_post_description),
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_post.post_image)
async def post_image(message: types.Message, state: FSMContext):
    await state.update_data(post_image=message.photo[0].file_id)
    await state.set_state(Create_post.post_tag)
    data = await state.get_data()
    data_post_name = data.get("post_name")
    data_post_description = data.get("post_description")
    await message.answer(text=_("create.post.tag").format(post_title=data_post_name,
                                                          post_description=data_post_description),
                         reply_markup=await admin_panel_keyboard_back_to_main_menu())


@router.message(Create_post.post_tag)
async def post_tag(message: types.Message, state: FSMContext):
    await state.update_data(post_tag=message.html_text)
    data = await state.get_data()

    user_id = int(message.from_user.id)
    current_post_name = str(data.get("post_name"))
    current_post_description = str(data.get("post_description"))
    current_post_image = str(data.get("post_image"))
    current_post_tag = str(data.get("post_tag"))
    current_time = datetime.datetime.now()
    create_date = str(current_time.date())
    create_time = str(current_time.time().replace(microsecond=0))
    current_user_name = await check_db_user_name(user_id=user_id)

    await create_post(post_name=current_post_name,
                      post_description=current_post_description,
                      post_image=current_post_image,
                      post_tag=current_post_tag,
                      user_name=current_user_name,
                      create_date=create_date,
                      create_time=create_time
                      )
    await message.answer_photo(photo=current_post_image,
                               caption=_("create.post.successfully_created_info").
                               format(post_title=current_post_name,
                                      post_description=current_post_description,
                                      post_tag=current_post_tag,
                                      post_creator=current_user_name,
                                      post_date_creation=create_date,
                                      post_time_creation=create_time),
                               reply_markup=await admin_panel_keyboard_back_to_main_menu())


def register_create_post_handlers(dp) -> None:
    dp.include_router(router)
