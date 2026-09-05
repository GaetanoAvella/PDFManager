import flet as ft
from state import AppState


async def open_file_picker(file_picker: ft.FilePicker, app_state: AppState) -> bool:
    file_picked = await file_picker.pick_files(
        allow_multiple=False,
        file_type=ft.FilePickerFileType.CUSTOM,
        allowed_extensions=["pdf"]
    )

    if not file_picked:
        return False

    file_path = file_picked[0].path
    if file_path is not None:
        app_state.add_doc(file_path)
        return True

    return False