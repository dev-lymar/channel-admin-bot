from handlers.start import start
from handlers.admin_panel import create_post, delete_post, main_menu
from handlers.admin_panel.create_user_role import create_user_role
from handlers.admin_panel.create_user_role.admin import admin, contenr_manager
from handlers.admin_panel.delete_user_role import delete_user_role


def register_routers(dp) -> None:
    start.register_start_command(dp)
    create_post.register_create_post_handlers(dp)
    delete_post.register_delete_post_handlers(dp)
    main_menu.register_main_menu_handlers(dp)
    create_user_role.register_create_user_role_handlers(dp)
    admin.register_load_user_role_admin_handlers(dp)
    contenr_manager.register_load_user_role_content_manager_handlers(dp)
    delete_user_role.register_delete_user_role_handlers(dp)
