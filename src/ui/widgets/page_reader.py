import flet as ft

from core import PdfDocument


READER_PAGE_WIDTH = 650
READER_PAGE_HEIGHT = 840


def build_reader(pdf_doc: PdfDocument, zoom_level: float) -> ft.Control:
    width = int(READER_PAGE_WIDTH * zoom_level)
    height = int(READER_PAGE_HEIGHT * zoom_level)

    list_view = ft.ListView(
        expand=True,
        spacing=16,
        padding=20,
        item_extent=height + 16,
        width=width + 40,
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