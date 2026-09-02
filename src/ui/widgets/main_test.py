import flet as ft
from page_grid import build_page_grid


def main(page: ft.Page):
    page.title = "Test Page Grid"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0d1117"
    page.padding = 0

    grid = build_page_grid(page, page_count=10)

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "Trascina una pagina sopra un'altra per riordinare",
                        size=14,
                        color="#8b949e",
                    ),
                    padding=20,
                ),
                grid,
            ],
            expand=True,
        )
    )


ft.run(main)