from aiogram.fsm.state import State, StatesGroup


class Create_user_role_admin(StatesGroup):
    """
    States for assigning the 'admin' role to a user.

    Attributes:
        user_id (State): State for receiving the user ID.
        user_name (State): State for receiving the username of the user.
    """
    user_id = State()
    user_name = State()


class Create_user_role_content_manager(StatesGroup):
    """
    States for assigning the 'content_manager' role to a user.

    Attributes:
        user_id (State): State for receiving the user ID.
        user_name (State): State for receiving the username of the user.
    """
    user_id = State()
    user_name = State()


class Delete_role_from_user(StatesGroup):
    """
    States for deleting a role from a user.

    Attributes:
        user_id (State): State for receiving the user ID.
        user_name (State): State for receiving the username of the user.
    """
    user_id = State()
    user_name = State()
