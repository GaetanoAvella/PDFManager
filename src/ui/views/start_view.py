import flet as ft


def build_start_view(on_click_callback) -> ft.Container:
    async def on_click(e):
        await on_click_callback()

    content_area = ft.Container(
        content=ft.Text(
            "Inserisci file",
            size=40,
        ),
        expand=True,
        padding=30,
        on_click=on_click,
    )

    return content_area