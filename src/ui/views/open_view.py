import flet as ft
from state import AppState
from widgets import build_page_grid


def build_open_view(app_state: AppState) -> ft.GridView:
        return build_page_grid(app_state)
