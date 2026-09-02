import flet as ft
from .pdf_page_card import build_page_card
from core import PdfDocument

def build_page_grid(page: ft.Page, pdf_doc: PdfDocument) -> ft.GridView:
    grid = ft.GridView(
        expand=True,
        max_extent=140,
        spacing=16,
        run_spacing=16,
        padding=20,
        controls=[]
    )

    def rebuild_grid():
        def build_cards_list() -> list[ft.Control]:
            cards = []
            grid_pos = 0
            for pdf_page in pdf_doc.pages_list:
                card = build_page_card(page, rebuild_grid, pdf_doc, pdf_page, grid_pos)
                grid_pos += 1
                cards.append(card)

            return cards

        grid.controls.clear()
        grid.controls = build_cards_list()
        page.update()

    rebuild_grid()
    return grid