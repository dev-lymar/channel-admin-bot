from handlers.start import start
from handlers.admin_panel import create_post, delete_post, main_menu


def register_routers(dp) -> None:
    start.register_start_command(dp)
    create_post.register_create_post_callback(dp)
    delete_post.register_delete_post_callback(dp)
    main_menu.register_main_menu_callback(dp)
