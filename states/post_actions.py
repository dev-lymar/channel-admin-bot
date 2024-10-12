from aiogram.fsm.state import State, StatesGroup


class Create_post(StatesGroup):
    """
    States for creating a post.

    Attributes:
        post_name (State): State for receiving the post's name.
        post_description (State): State for receiving the post's description.
        post_image (State): State for receiving the post's image.
        post_tag (State): State for receiving the post's tag.
    """
    post_name = State()
    post_description = State()
    post_image = State()
    post_tag = State()


class Change_post(StatesGroup):
    """
    States for editing an existing post.

    Attributes:
        post_id (State): State for receiving the post ID to edit.
        post_name (State): State for receiving the new name of the post.
        post_description (State): State for receiving the new description of the post.
        post_image (State): State for receiving the new image of the post.
        post_tag (State): State for receiving the new tag of the post.
    """
    post_id = State()
    post_name = State()
    post_description = State()
    post_image = State()
    post_tag = State()


class Delete_post(StatesGroup):
    """
    State for deleting a post.

    Attributes:
        post_id (State): State for receiving the ID of the post to be deleted.
    """
    post_id = State()


class Publish_post(StatesGroup):
    """
    State for publishing a post.

    Attributes:
        post_id (State): State for receiving the ID of the post to be published.
    """
    post_id = State()


class Check_post(StatesGroup):
    """
    State for checking a post's details.

    Attributes:
        post_id (State): State for receiving the ID of the post to check.
    """
    post_id = State()
