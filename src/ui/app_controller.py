from typing import Callable

import flet as ft
from state import AppView, AppState
from ui.views import view_router
from widgets import SideBar


class AppController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_state: AppState = AppState()
        self.active_view: AppView | None = None

        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.window.maximized = True
        self.page.bgcolor = "#0d1117"
        self.page.padding = 12

        self.file_picker = ft.FilePicker()
        self.page.services.append(self.file_picker)

        self.side_bar: SideBar = SideBar()
        self.content_area: ft.Container = ft.Container(expand=True)

        page.add(
            ft.Row(
                expand=True,
                controls=[self.side_bar.control, ft.VerticalDivider(width=1), self.content_area],
            )
        )

        self.refresh_view()

    def refresh_view(self, force_refresh: bool = False):
        real_current_view = self.app_state.get_active_view()
        if force_refresh or self.active_view != real_current_view:
            build_view: Callable[[AppController], None] = view_router.build_view(real_current_view)
            build_view(self)
            self.active_view = real_current_view
            self.page.update()

    async def open_file_picker(self) -> bool:
        file_picked = await self.file_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["pdf"]
        )

        if not file_picked:
            return False

        file_path = file_picked[0].path
        if file_path is not None:
            self.app_state.add_doc(file_path)
            return True

        return False
