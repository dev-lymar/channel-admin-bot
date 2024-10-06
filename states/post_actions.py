from aiogram.fsm.state import State, StatesGroup


class Create_post(StatesGroup):
    post_name = State()
    post_description = State()
    post_image = State()
    post_tag = State()
    create_date = State()
    create_time = State()
