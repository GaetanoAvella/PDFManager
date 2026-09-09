import flet as ft

from core import PdfDocument
from state import AppState


def build_reader(pdf_doc: PdfDocument) -> ft.ListView:
    return ft.ListView(
        expand=True,
        spacing=16,
        padding=20,
        controls=[
            build_reader_page(page)
            for page in pdf_doc.get_pages()
        ]
    )

def build_reader_page(page: PdfDocument.PdfPage) -> ft.Control:
    return ft.Container(
        content=ft.Image(
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