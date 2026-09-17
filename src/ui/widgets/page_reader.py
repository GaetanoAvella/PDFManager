import flet as ft

from core import PdfDocument


READER_PAGE_WIDTH = 650
READER_PAGE_HEIGHT = 840


def build_reader(pdf_doc: PdfDocument, zoom_level: float, on_scroll=None) -> ft.Control:
    width = int(READER_PAGE_WIDTH * zoom_level)
    height = int(READER_PAGE_HEIGHT * zoom_level)
    item_extent = height + 16

    list_view = ft.ListView(
        build_controls_on_demand=True,
        expand=True,
        spacing=16,
        padding=20,
        item_extent=item_extent,
        width=width + 40,
        on_scroll=on_scroll,
        controls=[
            build_reader_page(page, width, height)
            for page in pdf_doc.get_pages()
        ]
    )

    return ft.Row(
        expand=True,
        scroll=ft.ScrollMode.ADAPTIVE,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[list_view],
    )

def build_reader_page(page: PdfDocument.PdfPage, width: int, height: int) -> ft.Control:
    return ft.Container(
        content=ft.Image(
            width=width,
            height=height,
            src=page.render_page_as_image_base64(scale=2.5),
            fit=ft.BoxFit.CONTAIN,
            border_radius=4
        ),
        bgcolor="#161b22",
        border=ft.Border.all(1, "#30363d"),
        border_radius=8,
        padding=8,
        alignment=ft.Alignment.CENTER,
    )