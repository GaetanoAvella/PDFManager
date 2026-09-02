import flet as ft
from core import PdfDocument
from ui.widgets import build_page_grid

def build_shell(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.maximized = True
    page.bgcolor = "#0d1117"
    page.padding = 12

    sections = [
        {"label": "Merge", "icon": ft.Icons.MERGE_TYPE_OUTLINED, "icon_selected": ft.Icons.MERGE_TYPE},
        {"label": "Edit", "icon": ft.Icons.REORDER_OUTLINED, "icon_selected": ft.Icons.REORDER},
    ]

    file_picker = ft.FilePicker()

    async def on_click_open_file(e):
        file_picked = await file_picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["pdf"]
        )
        file_path = file_picked[0].path
        if file_path is not None:
            pdf_doc = PdfDocument(file_path)
            content_area.content=build_page_grid(page, pdf_doc)
            content_area.on_click = None
            page.update()


    content_area = ft.Container(
        content=ft.Text(
            "Inserisci file",
            size=40,
        ),
        expand=True,
        padding=30,
        on_click=on_click_open_file
    )

    def on_nav_change(e):
        sel_index = e.control.selected_index
        sel_label = sections[sel_index]["label"]

        page.update()

    nav_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=90,
        min_extended_width=180,
        bgcolor="#161b22",
        indicator_color="#238636",
        destinations=[
            ft.NavigationRailDestination(
                icon=s["icon"],
                selected_icon=s["icon_selected"],
                label=s["label"],
            )
            for s in sections
        ],
        on_change=on_nav_change
    )

    page.add(
        ft.Row(
            expand=True,
            controls=[
                nav_rail,
                ft.VerticalDivider(width=1, color="#30363d"),
                content_area
            ]
        )
    )

ft.run(build_shell)