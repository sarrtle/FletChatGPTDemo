"""
Reusable components
"""

from typing import Callable
import flet as ft  # type: ignore
from color_scheme import color_config


def appbar(page: ft.Page, navigation_menu: ft.NavigationDrawer):
    """
    Appbar component
    """

    return ft.AppBar(
        leading=ft.IconButton(
            icon=ft.icons.MENU,
            on_click=lambda _: page.open(navigation_menu),
            icon_color=color_config.TEXT_COLOR,
            hover_color=ft.colors.TRANSPARENT,
            highlight_color=ft.colors.with_opacity(0.3, color=color_config.TEXT_COLOR),
        ),
        title=ft.Text(
            value="Greetings New",
            size=14,
            weight=ft.FontWeight.BOLD,
            animate_opacity=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_IN),
            color=color_config.TEXT_COLOR,
            selectable=True,
        ),
        center_title=True,
        force_material_transparency=True,
    )


def message_content():
    """
    Message content of bot and the user
    """

    return ft.ListView(spacing=12, auto_scroll=True, expand=True)


def user_input_options(page: ft.Page, message_container: ft.ListView):
    """
    User input options such as sending text, file or images
    """

    def on_send_click(_: ft.ControlEvent):
        # DO SOMETHING HERE ON SEND REQUEST
        switch_send.content = loading_response_button
        switch_send.update()

        user_message(page, message_container, text_field.value, "text")
        text_field.value = ""
        text_field.update()

    def change_input(_: ft.ControlEvent):
        if text_field.value and switch_send.content == mic_button:
            switch_send.content = send_button
            switch_send.update()
        else:
            if switch_send.content != mic_button and not text_field.value:
                switch_send.content = mic_button
                switch_send.update()

    def on_stop_click(_: ft.ControlEvent):
        switch_send.content = mic_button
        switch_send.update()

    send_button = ft.IconButton(
        icon=ft.icons.ARROW_UPWARD,
        icon_color=color_config.TEXT_COLOR,
        hover_color=ft.colors.TRANSPARENT,
        highlight_color=ft.colors.with_opacity(0.3, color=color_config.TEXT_COLOR),
        padding=12,
        on_click=on_send_click,
    )

    mic_button = ft.IconButton(
        icon=ft.icons.MIC,
        icon_color=color_config.TEXT_COLOR,
        hover_color=ft.colors.TRANSPARENT,
        highlight_color=ft.colors.with_opacity(0.3, color=color_config.TEXT_COLOR),
        padding=12,
        offset=ft.transform.Offset(0, 0),
    )

    loading_response_button = ft.IconButton(
        icon=ft.icons.STOP,
        icon_color=color_config.TEXT_COLOR,
        hover_color=ft.colors.TRANSPARENT,
        highlight_color=ft.colors.with_opacity(0.3, color=color_config.TEXT_COLOR),
        padding=12,
        on_click=on_stop_click,
    )

    text_field = ft.TextField(
        expand=True,
        hint_text="Type your message or /help",
        hint_style=ft.TextStyle(
            size=14,
            color=ft.colors.with_opacity(0.5, color_config.TEXT_COLOR_MESSAGE_BUBBLE),
        ),
        color=color_config.TEXT_COLOR_MESSAGE_BUBBLE,
        bgcolor=color_config.INPUT_FIELDS_ICONS_COLOR,
        border_radius=26,
        content_padding=ft.Padding(top=9, left=15, bottom=9, right=15),
        text_size=15,
        multiline=True,
        max_lines=5,
        shift_enter=True,
        focused_border_color=ft.colors.TRANSPARENT,
        border_color=ft.colors.TRANSPARENT,
        cursor_color=color_config.TEXT_COLOR_MESSAGE_BUBBLE,
        selection_color=ft.colors.BLUE_300,
        # animate_size=ft.Animation(200, curve=ft.AnimationCurve.LINEAR),
        on_change=change_input,
    )

    switch_send = ft.AnimatedSwitcher(
        content=mic_button,
        duration=200,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_IN,
        switch_out_curve=ft.AnimationCurve.BOUNCE_OUT,
        transition=ft.AnimatedSwitcherTransition.SCALE,
    )

    return ft.Container(
        content=ft.Row(
            controls=[text_field, switch_send],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=ft.Padding(top=0, left=15, bottom=0, right=15),
        margin=ft.Margin(top=0, left=0, bottom=10, right=0),
    )


def user_message(
    page: ft.Page, message_container: ft.ListView, message: str, message_type: str
):
    """
    Message of the user

    Parameters:
    - message_container = flet ListView
    - message = the message string
    - message_type = whether the user input is a text, file or an image
    """

    if message_type == "text":
        message_container.controls.append(
            ft.Container(
                content=ft.Text(
                    value=message,
                    size=16,
                    text_align=ft.TextAlign.RIGHT,
                    color=color_config.TEXT_COLOR_MESSAGE_BUBBLE,
                ),
                bgcolor=color_config.PRIMARY,
                padding=ft.Padding(top=15, left=24, bottom=15, right=24),
                border_radius=26,
                margin=ft.Margin(top=0, left=36, bottom=0, right=15),
                ink=True,
                ink_color=ft.colors.GREY_200,
                on_long_press=lambda _: page.open(show_user_message_menu(page)),
            )
        )
    message_container.update()


def bot_message(
    page: ft.Page, message_container: ft.ListView, message: str, message_type: str
):
    """
    Message of the bot
    """

    if message_type == "text":
        message_container.controls.append(
            ft.Container(
                content=ft.Markdown(
                    value=message,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    code_theme=color_config.CODE_THEME,
                ),
                padding=15,
                ink=True,
                ink_color=ft.colors.BLACK26,
                on_long_press=lambda _x: page.open(show_bot_message_menu()),
                theme=ft.Theme(
                    text_theme=ft.TextTheme(
                        display_large=ft.TextStyle(
                            size=34,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Large display text
                        display_medium=ft.TextStyle(
                            size=30,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Medium display text
                        display_small=ft.TextStyle(
                            size=26,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Small display text
                        title_large=ft.TextStyle(
                            size=24,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # H2
                        title_medium=ft.TextStyle(
                            size=22,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # H3
                        title_small=ft.TextStyle(
                            size=20,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # H4
                        headline_large=ft.TextStyle(
                            size=28,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # H1
                        headline_medium=ft.TextStyle(
                            size=24,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # H2
                        headline_small=ft.TextStyle(
                            size=20,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # H3
                        body_large=ft.TextStyle(
                            size=18,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Body text
                        body_medium=ft.TextStyle(
                            size=16,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Body text
                        body_small=ft.TextStyle(
                            size=14,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Smaller body text
                        label_large=ft.TextStyle(
                            size=18,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Large labels
                        label_medium=ft.TextStyle(
                            size=16,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Medium labels
                        label_small=ft.TextStyle(
                            size=14,
                            color=color_config.TEXT_COLOR,
                            font_family="Montserrat",
                        ),  # Small labels
                    )
                ),
            )
        )
    message_container.update()


def navigation_drawer(page: ft.Page):
    """
    Navigation menu
    """

    new_chat_button = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.OPEN_IN_NEW, color=color_config.TEXT_COLOR),
                ft.Text(value="New Chat", color=color_config.TEXT_COLOR),
            ],
        ),
        padding=16,
        ink=True,
        on_click=lambda _: "",
    )
    settings_button = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.SETTINGS, color=color_config.TEXT_COLOR),
                ft.Text(value="Settings", color=color_config.TEXT_COLOR),
            ],
        ),
        padding=16,
        ink=True,
        on_click=lambda _: page.go("/settings"),
    )

    settings_container = ft.Container(
        content=ft.Column(
            controls=[
                new_chat_button,
                settings_button,
            ],
        ),
        border=ft.Border(top=ft.BorderSide(width=1, color=color_config.TEXT_COLOR)),
    )

    message_history_container = ft.ListView()
    message_history_container.controls.append(message_history_date("Today"))
    message_history_container.controls.append(message_history_item("Hello, World!"))
    message_history_container.controls.append(
        message_history_item("Hello, Another World!")
    )
    message_history_container.controls.append(message_history_date("Yesterday"))
    message_history_container.controls.append(
        message_history_item("Best library for mobile app development")
    )

    navigation_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                value="Message History",
                                weight=ft.FontWeight.BOLD,
                                size=16,
                                color=color_config.TEXT_COLOR,
                            ),
                            padding=ft.Padding(top=0, left=16, bottom=0, right=16),
                        ),
                        message_history_container,
                    ],
                ),
                settings_container,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor=color_config.BACKGROUND_COLOR,
        padding=ft.Padding(top=16, left=0, bottom=16, right=0),
        height=page.height,
    )

    return ft.NavigationDrawer(controls=[navigation_container])


def message_history_item(title: str):
    """
    Message history item in the navbar
    """

    def on_message_history_clicked(_: ft.ControlEvent):
        """
        TODO: CLEAR THE MESSAGE CONTENT AND ADD SELECTED COLOR
        """

    message_item = ft.Container(
        content=ft.Text(
            value=title,
            size=14,
            color=color_config.TEXT_COLOR,
            expand=True,
            overflow=ft.TextOverflow.ELLIPSIS,
        ),
        padding=16,
        ink=True,
        on_click=on_message_history_clicked,
    )

    return message_item


def message_history_date(date: str):
    """Message history date"""
    return ft.Container(
        content=ft.Text(
            value=date,
            size=12,
            color=ft.colors.with_opacity(0.4, color_config.TEXT_COLOR),
            expand=True,
        ),
        padding=ft.Padding(top=16, left=16, bottom=0, right=16),
    )


def show_user_message_menu(page: ft.Page):
    """
    Menu option for editing the messages and history
    """

    def button(
        button_name: str, icon: ft.Icon, on_click: Callable[[ft.ControlEvent], None]
    ):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=icon, color=color_config.TEXT_COLOR),
                    ft.Text(
                        value=button_name,
                        color=color_config.TEXT_COLOR,
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ]
            ),
            padding=20,
            ink=True,
            on_click=on_click,
        )

    def test(_):
        """none"""

    def go(_):
        page.go("/select_text")

    return ft.BottomSheet(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    button("Copy", ft.icons.COPY_SHARP, test),
                    button(
                        "Select Text",
                        ft.icons.TEXT_FIELDS_OUTLINED,
                        go,
                    ),
                    button("Edit Message", ft.icons.EDIT_SHARP, test),
                ],
                alignment=ft.MainAxisAlignment.END,
                tight=True,
                spacing=0,
            ),
            border_radius=ft.BorderRadius(
                top_left=32, top_right=32, bottom_left=0, bottom_right=0
            ),
        ),
        bgcolor=color_config.BACKGROUND_COLOR,
    )


def show_bot_message_menu():
    """
    Menu options for bot message
    """

    def button(button_name: str, icon: ft.Icon):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=icon, color=color_config.TEXT_COLOR),
                    ft.Text(
                        value=button_name,
                        color=color_config.TEXT_COLOR,
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ]
            ),
            padding=20,
            ink=True,
            on_click="",
        )

    return ft.BottomSheet(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    button("Copy", ft.icons.COPY_SHARP),
                    button("Select Text", ft.icons.TEXT_FIELDS_OUTLINED),
                    button("Regenerate Response", ft.icons.REPEAT_SHARP),
                    button("Read Aloud", ft.icons.MULTITRACK_AUDIO_SHARP),
                ],
                alignment=ft.MainAxisAlignment.END,
                tight=True,
                spacing=0,
            ),
            border_radius=ft.BorderRadius(
                top_left=32, top_right=32, bottom_left=0, bottom_right=0
            ),
        ),
        bgcolor=color_config.BACKGROUND_COLOR,
    )


# I will be putting more components here lol
def settings_page():
    """
    Settings page for the app
    """

    settings_container = ft.Container(
        content=ft.Column(
            controls=[
                # container for each settings
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Model Instruction", color=color_config.TEXT_COLOR),
                            ft.TextField(
                                multiline=True,
                                min_lines=5,
                                max_lines=5,
                                hint_text="Act like a [someone], you must be [something]"
                                " and be [what you want] ...",
                                hint_style=ft.TextStyle(color=color_config.TEXT_COLOR),
                                color=color_config.TEXT_COLOR,
                                border_color=color_config.TEXT_COLOR,
                            ),
                        ]
                    ),
                    bgcolor=color_config.CONTAINER_COLOR,
                    padding=15,
                    border_radius=16,
                ),
                # for the api url
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Api Url", color=color_config.TEXT_COLOR),
                            ft.TextField(
                                hint_text="enter your api url here",
                                hint_style=ft.TextStyle(color=color_config.TEXT_COLOR),
                                color=color_config.TEXT_COLOR,
                                border_color=color_config.TEXT_COLOR,
                            ),
                        ]
                    ),
                    bgcolor=color_config.CONTAINER_COLOR,
                    padding=15,
                    border_radius=16,
                ),
                # for the token
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("Api Token", color=color_config.TEXT_COLOR),
                                    ft.Switch(
                                        value=True,
                                        tooltip="Turn off if no api token needed for your api.",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.TextField(
                                hint_text="enter your api token here",
                                hint_style=ft.TextStyle(color=color_config.TEXT_COLOR),
                                color=color_config.TEXT_COLOR,
                                border_color=color_config.TEXT_COLOR,
                            ),
                        ]
                    ),
                    bgcolor=color_config.CONTAINER_COLOR,
                    padding=15,
                    border_radius=16,
                ),
                # for choosing voice models
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Voice Model", color=color_config.TEXT_COLOR),
                            ft.Dropdown(
                                value="Alloy",
                                border_color=color_config.TEXT_COLOR,
                                bgcolor=color_config.PRIMARY,
                                filled=True,
                                fill_color=color_config.CONTAINER_COLOR,
                                icon_enabled_color=color_config.TEXT_COLOR,
                                options=[
                                    ft.dropdown.Option(
                                        "Alloy",
                                        text_style=ft.TextStyle(
                                            color=color_config.TEXT_COLOR,
                                        ),
                                    ),
                                    ft.dropdown.Option(
                                        "Echo",
                                        text_style=ft.TextStyle(
                                            color=color_config.TEXT_COLOR
                                        ),
                                    ),
                                    ft.dropdown.Option(
                                        "Fable",
                                        text_style=ft.TextStyle(
                                            color=color_config.TEXT_COLOR
                                        ),
                                    ),
                                    ft.dropdown.Option(
                                        "Onyx",
                                        text_style=ft.TextStyle(
                                            color=color_config.TEXT_COLOR
                                        ),
                                    ),
                                    ft.dropdown.Option(
                                        "Nova",
                                        text_style=ft.TextStyle(
                                            color=color_config.TEXT_COLOR
                                        ),
                                    ),
                                    ft.dropdown.Option(
                                        "Shimmer",
                                        text_style=ft.TextStyle(
                                            color=color_config.TEXT_COLOR
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    bgcolor=color_config.CONTAINER_COLOR,
                    padding=15,
                    border_radius=16,
                ),
            ],
            spacing=12,
            expand=True,
        )
    )

    return ft.View(
        "/settings",
        controls=[settings_container],
        appbar=ft.AppBar(
            title=ft.Text("Settings", size=16),
            bgcolor=ft.colors.TRANSPARENT,
            color=color_config.TEXT_COLOR,
            force_material_transparency=True,
        ),
        bgcolor=color_config.BACKGROUND_COLOR,
        scroll=ft.ScrollMode.AUTO,
    )
