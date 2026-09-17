from typing import TYPE_CHECKING

import flet as ft

from state import AppView
from widgets import build_page_grid

if TYPE_CHECKING:
    from ui.app_controller import AppController


def build_edit_view(app_controller: "AppController"):
    def on_click_close_button(e):
        app_controller.app_state.set_active_view(AppView.START)
        app_controller.refresh_view()

    pdf = app_controller.app_state.get_active_doc()

    if pdf is None:
        return

    app_controller.content_area.content = build_page_grid(app_controller.app_state)

    app_controller.side_bar.clear()

    app_controller.side_bar.add_change_view_button(ft.IconButton(
        icon=ft.Icons.MOUSE_OUTLINED,
    ))

    app_controller.side_bar.add_change_view_button(ft.IconButton(
        icon=ft.Icons.DELETE_OUTLINED,
    ))

    app_controller.side_bar.add_change_view_button(ft.IconButton(
        icon=ft.Icons.RESET_TV_OUTLINED,
    ))

    app_controller.side_bar.add_change_view_button(ft.IconButton(
        icon=ft.Icons.SAVE_OUTLINED,
    ))

    app_controller.side_bar.add_change_view_button(ft.IconButton(
        icon=ft.Icons.CLOSE_OUTLINED,
        on_click=on_click_close_button
    ))

    app_controller.side_bar.refresh()

