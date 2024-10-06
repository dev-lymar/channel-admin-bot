from aiogram.fsm.state import State, StatesGroup


class Create_post(StatesGroup):
    post_name = State()
    post_description = State()
    post_image = State()
    post_tag = State()


class Change_post(StatesGroup):
    post_id = State()
    post_name = State()
    post_description = State()
    post_image = State()
    post_tag = State()


class Delete_post(StatesGroup):
    post_id = State()
