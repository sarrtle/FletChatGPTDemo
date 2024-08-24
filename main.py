"""
Main application
"""

import flet as ft  # type: ignore

from components import (
    appbar,
    bot_message,
    message_content,
    navigation_drawer,
    user_input_options,
    user_message,
    settings_page,
)

from color_scheme import color_config


# generate random messages
def generate_message(page: ft.Page, message_container: ft.ListView):
    """
    Generate sample message
    """

    messages = [
        {"role": "user", "content": "Hi!"},
        {"role": "assistant", "content": "Hello! what can I do for you today?"},
        {
            "role": "user",
            "content": "Generate me some sleek ui code for my flutter app",
        },
        {
            "role": "assistant",
            "content": "Sure, let me do that for you.\n```python\n# here's how you print number from one to ten\nfor i in range(10):\n\tprint(i)\n```",
        },
        {
            "role": "user",
            "content": "Thanks! That is awesome, let me try that.",
        },
        {
            "role": "assistant",
            "content": "Great, if you need anything, just ask right away.",
        },
    ]
    for message in messages:
        if message.get("role") == "user":
            user_message(
                page=page,
                message_container=message_container,
                message=message.get("content", ""),
                message_type="text",
            )
        else:
            bot_message(
                page=page,
                message_container=message_container,
                message=message.get("content", ""),
                message_type="text",
            )


async def main(page: ft.Page):
    """
    run the main application
    """

    # for debugging purposes
    page.window.always_on_top = True

    # set color theme
    color_config.mode = page.platform_brightness.value

    # set font
    page.fonts = {"Montserrat": "fonts/Montserrat-Regular.ttf"}
    page.theme = ft.Theme(font_family="Montserrat")

    message_container = message_content()

    # add message logs on navigation menu
    navigation_menu = navigation_drawer(page)

    # main app
    main_app = ft.View(
        "/",
        controls=[
            message_container,
            user_input_options(page, message_container=message_container),
        ],
        appbar=appbar(page=page, navigation_menu=navigation_menu),
        drawer=navigation_menu,
        bgcolor=color_config.BACKGROUND_COLOR,
        padding=0,
    )

    # settings
    settings_page_view = settings_page()

    # select text
    select_text_page = ft.View(
        "/select_text",
        controls=[
            ft.Text(
                "This is a sample text",
                size=16,
                color=color_config.TEXT_COLOR,
                selectable=True,
            )
        ],
        appbar=ft.AppBar(
            title=ft.Text("Select Text", size=24, color=color_config.TEXT_COLOR)
        ),
    )

    def route_change(_: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(main_app)

        if page.route == "/select_text":
            page.views.append(select_text_page)

        if page.route == "/settings":
            page.views.append(settings_page_view)

        page.update()

    def view_pop(_: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

    message_container.did_mount = lambda: generate_message(page, message_container)


ft.app(main)
