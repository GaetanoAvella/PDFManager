import flet as ft


def build_start_view() -> ft.Container:
    return ft.Container(
        content=ft.Text(
            "Trascina file qui per iniziare",
            size=40,
        ),
        expand=True,
        padding=30,
    )