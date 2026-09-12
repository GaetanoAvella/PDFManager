import flet as ft
from ui.widgets import *
from ui.views import *
from state import AppState, AppView


def build_shell(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.maximized = True
    page.bgcolor = "#0d1117"
    page.padding = 12

    file_picker = ft.FilePicker()
    page.services.append(file_picker)

    app_state = AppState()
    content_area = build_start_view()

    def build_view_content(view: AppView) -> ft.Control:
        match view:
            case AppView.START:
                return build_start_view()
            case AppView.OPEN:
                return build_read_view(app_state)
            case AppView.EDIT:
                return build_edit_view(app_state)

        return build_start_view()

    def switch_view(view: AppView):
        side_bar.data = view
        side_bar.controls = build_side_bar_controls(view, handle_action)
        side_bar.update()

        content_area.content = build_view_content(view)
        page.update()

    async def handle_action(action: str):
        match action:
            case "open":
                if await open_file_picker(file_picker, app_state):
                    switch_view(AppView.OPEN)
            case "edit":
                if await open_file_picker(file_picker, app_state):
                    switch_view(AppView.EDIT)
            case "merge":
                pass # TODO merge view
            case "zoom_out":
                zoom = app_state.get_active_doc_zoom() - 0.2
                if zoom > 0.2:
                    app_state.set_active_doc_zoom(zoom)
                    switch_view(AppView.OPEN)
            case "zoom_in":
                zoom = app_state.get_active_doc_zoom() + 0.2
                if zoom < 3.0:
                    app_state.set_active_doc_zoom(zoom)
                    switch_view(AppView.OPEN)

    side_bar = build_side_bar(AppView.START, handle_action)

    page.add(
        ft.Row(
            expand=True,
            controls=[
                side_bar,
                ft.VerticalDivider(width=1, color="#30363d"),
                content_area
            ]
        )
    )