import flet as ft

from state import AppState
from widgets import build_reader


def build_read_view(app_state: AppState) -> ft.Control:
    pdf_doc = app_state.get_active_doc()
    zoom = app_state.get_active_doc_zoom()

    if pdf_doc is None:
        return ft.Text("No PDF file")

    return build_reader(pdf_doc, zoom)