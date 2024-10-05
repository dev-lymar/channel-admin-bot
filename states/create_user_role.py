from aiogram.fsm.state import State, StatesGroup


class Create_user_role_admin(StatesGroup):
    user_id = State()


class Create_user_role_content_manager(StatesGroup):
    user_id = State()
