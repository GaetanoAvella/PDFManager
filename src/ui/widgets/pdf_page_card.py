import flet as ft
from core import PdfDocument


def build_page_card(page: ft.Page, rebuild_grid , pdf_doc: PdfDocument, pdf_page: PdfDocument.PdfPage, position_in_grid: int) -> ft.Control:
    card_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(ft.Icons.DESCRIPTION_OUTLINED, size=32, color="#8b949e"),
                ft.Text(
                    f"PDF PAGE {pdf_page.page_position}",
                    size=11,
                    color="#c9d1d9",
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.W_500,
                ),
                ft.Text(
                    f"{position_in_grid}",
                    size=10,
                    color="#6e7681",
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            tight=True,
        ),
        width=110,
        height=140,
        bgcolor="#161b22",
        border=ft.Border.all(1, "#30363d"),
        border_radius=8,
        alignment=ft.Alignment.CENTER,
    )

    placeholder_when_dragging = ft.Container(
        width=110,
        height=140,
        bgcolor="#0d1117",
        border=ft.Border.all(1, "#21262d"),
        border_radius=8,
    )

    dragged_item = ft.Container(
        content=card_content.content,
        width=110,
        height=140,
        bgcolor="#1f2937",
        border=ft.Border.all(2, "#58a6ff"),
        border_radius=8,
        opacity=0.85,
    )

    def on_will_accept(e):
        e.control.content.border = ft.Border.all(2, "#58a6ff")
        page.update()

    def on_leave(e):
        e.control.content.border = ft.Border.all(1, "#30363d")
        page.update()

    def on_accept(e):
        source_control = e.src

        source_position = int(source_control.data)
        target_position = position_in_grid

        if source_position == target_position:
            return

        moved_id = pdf_doc.remove_page(source_position)
        pdf_doc.insert_page(target_position, moved_id)
        rebuild_grid()

    drag_target = ft.DragTarget(
        group="pdf_page",
        content=card_content,
        on_accept=on_accept,
        on_leave=on_leave,
        on_will_accept=on_will_accept,
    )

    draggable = ft.Draggable(
        group="pdf_page",
        data=str(position_in_grid),
        content=drag_target,
        content_when_dragging=placeholder_when_dragging,
        content_feedback=dragged_item,
    )

    return draggable