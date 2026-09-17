from typing import TYPE_CHECKING

import flet as ft

from state import AppView
from ui.widgets import build_reader
from widgets.page_reader import READER_PAGE_HEIGHT

if TYPE_CHECKING:
    from ui.app_controller import AppController


def build_read_view(app_controller: "AppController"):
    async def on_blur_text_field(e):
        try:
            req_value = int(e.control.value)
        except ValueError:
            req_value = int(e.control.data)
            e.control.value = req_value
            return

        if req_value == int(e.control.data):
            return

        if req_value < 1 or req_value > total_pages:
            e.control.value = int(e.control.data)

        new_page = max(min(req_value, total_pages), 1)
        await go_to_page(new_page)

    async def on_click_next_page(e):
        curr_page = int(current_page_text.data)
        if curr_page == total_pages:
            return
        await go_to_page(curr_page + 1)
        current_page_text.value = str(curr_page + 1)
        current_page_text.data = str(curr_page + 1)

    async def on_click_prev_page(e):
        curr_page = int(current_page_text.data)
        if curr_page == 1:
            return
        await go_to_page(curr_page - 1)
        current_page_text.value = str(curr_page - 1)
        current_page_text.data = str(curr_page - 1)

    def on_click_edit_button(e):
        app_controller.app_state.set_active_view(AppView.EDIT)
        app_controller.refresh_view()

    def on_click_close_button(e):
        app_controller.app_state.set_active_view(AppView.START)
        app_controller.refresh_view()

    def on_click_zoom_in_button(e):
        app_controller.app_state.set_active_doc_zoom(
            min(app_controller.app_state.get_active_doc_zoom() + 0.2, 3.0)
        )
        app_controller.refresh_view(True)

    def on_click_zoom_out_button(e):
        app_controller.app_state.set_active_doc_zoom(
            max(app_controller.app_state.get_active_doc_zoom() - 0.2, 0.2)
        )
        app_controller.refresh_view(True)

    def on_scroll(e: ft.OnScrollEvent):
        current_page = int(e.pixels // item_extent) + 1
        current_page = max(1, min(current_page, total_pages))
        current_page_text.value = str(current_page)
        current_page_text.data = str(current_page)
        current_page_text.update()

    async def go_to_page(to_page: int):
        offset = (to_page - 1) * item_extent
        await list_view.scroll_to(offset=offset)
        current_page_text.data = str(to_page)

    pdf_doc = app_controller.app_state.get_active_doc()
    zoom = app_controller.app_state.get_active_doc_zoom()

    if pdf_doc is None:
        return

    total_pages = pdf_doc.pdf_pages
    item_extent = (READER_PAGE_HEIGHT * zoom) + 16

    reader = build_reader(pdf_doc, zoom, on_scroll)
    list_view: ft.ListView = reader.controls[0]
    app_controller.content_area.content = reader

    app_controller.side_bar.clear()

    app_controller.side_bar.add_change_view_button(ft.Button(
        content="Edit",
        on_click=on_click_edit_button,
    ))

    app_controller.side_bar.add_change_view_button(ft.Button(
        content="Close",
        on_click=on_click_close_button,
    ))

    #current page
    current_page_text = ft.TextField(
        value=str(1),
        data=str(1),
        on_blur=on_blur_text_field
    )
    app_controller.side_bar.add_utility(current_page_text)

    #total pages
    app_controller.side_bar.add_utility(ft.Text(
        value=str(total_pages)
    ))

    app_controller.side_bar.add_utility(ft.IconButton(
        icon=ft.Icons.ARROW_UPWARD_OUTLINED,
        on_click=on_click_prev_page
    ))

    app_controller.side_bar.add_utility(ft.IconButton(
        icon=ft.Icons.ARROW_DOWNWARD_OUTLINED,
        on_click=on_click_next_page
    ))

    app_controller.side_bar.add_utility(ft.IconButton(
        icon=ft.Icons.ZOOM_IN_OUTLINED,
        on_click=on_click_zoom_in_button
    ))

    app_controller.side_bar.add_utility(ft.IconButton(
        icon=ft.Icons.ZOOM_OUT_OUTLINED,
        on_click=on_click_zoom_out_button
    ))

    app_controller.side_bar.refresh()