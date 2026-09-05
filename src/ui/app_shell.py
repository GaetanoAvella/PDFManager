import flet as ft
from ui.widgets import *
from ui.views import *
from state import AppState


def build_shell(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.maximized = True
    page.bgcolor = "#0d1117"
    page.padding = 12

    file_picker = ft.FilePicker()
    page.services.append(file_picker)

    app_state = AppState()

    content_area = ft.Container(expand=True)

    def show_start_view():
        content_area.content = build_start_view(handle_open_file)
        page.update()

    def show_open_view():
        content_area.content = build_open_view(app_state)
        page.update()

    async def handle_open_file():
        if await open_file_picker(file_picker, app_state):
            nav_rail.destinations = build_nav_destinations("FILE_OPEN")
            nav_rail.data="FILE_OPEN"
            show_open_view()

    async def on_nav_change(e):
        page_state = e.control.data
        selected_section = e.control.selected_index

        match page_state:
            case "START":
                if selected_section == 0:
                    await handle_open_file()

    nav_rail = build_navigation_rail("START", on_nav_change)

    show_start_view()

    page.add(
        ft.Row(
            expand=True,
            controls=[
                nav_rail,
                ft.VerticalDivider(width=1, color="#30363d"),
                content_area
            ]
        )
    )