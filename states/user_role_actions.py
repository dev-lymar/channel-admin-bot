from aiogram.fsm.state import State, StatesGroup


class Create_user_role_admin(StatesGroup):
    user_id = State()
    user_name = State()


class Create_user_role_content_manager(StatesGroup):
    user_id = State()
    user_name = State()


class Delete_role_from_user(StatesGroup):
    user_id = State()
    user_name = State()
