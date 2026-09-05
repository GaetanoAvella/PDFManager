import flet as ft
from state import AppState


async def open_file_picker(file_picker: ft.FilePicker, app_state: AppState) -> bool:
    file_picked = await file_picker.pick_files(
        allow_multiple=False,
        file_type=ft.FilePickerFileType.CUSTOM,
        allowed_extensions=["pdf"]
    )

    if not file_picked or file_picked[0].path is None:
        return False

    app_state.add_doc(file_picked[0].path)
    return True