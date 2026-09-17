from typing import TYPE_CHECKING
import flet as ft
from state import AppView

if TYPE_CHECKING:
    from ui.app_controller import AppController


def build_start_view(app_controller: "AppController"):
    async def on_click_open_button(e):
        await app_controller.open_file_picker()
        app_controller.app_state.set_active_view(AppView.READ)
        app_controller.refresh_view()

    async def on_click_edit_button(e):
        await app_controller.open_file_picker()
        app_controller.app_state.set_active_view(AppView.EDIT)
        app_controller.refresh_view()

    def on_click_merge_button(e):
        app_controller.app_state.set_active_view(AppView.MERGE)
        app_controller.refresh_view()

    app_controller.content_area.content = ft.Container(
        content=ft.Text(
            "Trascina file qui per iniziare",
            size=40,
        ),
        expand=True,
        padding=30,
    )

    app_controller.side_bar.clear()

    app_controller.side_bar.add_change_view_button(ft.Button(
        content="Open",
        on_click=on_click_open_button,
    ))

    app_controller.side_bar.add_change_view_button(ft.Button(
        content="Edit",
        on_click=on_click_edit_button,
    ))

    app_controller.side_bar.add_change_view_button(ft.Button(
        content="Merge",
        on_click=on_click_merge_button,
    ))

    app_controller.side_bar.refresh()