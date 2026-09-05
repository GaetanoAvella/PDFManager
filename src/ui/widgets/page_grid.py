import flet as ft

from state import AppState
from .pdf_page_card import build_page_card

def build_page_grid(app_state: AppState) -> ft.GridView:
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
            pdf_doc = app_state.get_active_doc()
            print(pdf_doc)
            if pdf_doc is not None:
                for pdf_page in pdf_doc.pages_list:
                    card = build_page_card(rebuild_grid, pdf_doc, pdf_page, grid_pos)
                    grid_pos += 1
                    cards.append(card)

            return cards

        grid.controls.clear()
        grid.controls = build_cards_list()

    rebuild_grid()
    return grid