from typing import Callable, Coroutine, Any
import flet as ft
from state import AppView


SECTIONS: dict[AppView, list[dict]] = {
    AppView.START: [
        {"label": "Open",   "action": "open"},  #one-shot
        {"label": "Edit",   "action": "edit"},  #one-shot
        {"label": "Merge",  "action": "merge"},  #one-shot
    ],
    AppView.OPEN: [
        {"label": "Zoom", "action": "zoom"}
    ],
    AppView.EDIT: [
        {"label": "Select", "action": "select"},  #on/off
        {"label": "Delete", "action": "delete"},  #one-shot
        {"label": "Reset",  "action": "reset"},  #one-shot
        {"label": "Save",   "action": "save"},  #one-shot
        {"label": "Close",  "action": "close"},  #one-shot
    ]
}


def build_side_bar(view: AppView, on_action: Callable[[str], Coroutine[Any, Any, None]]) -> ft.Column:
    side_bar = ft.Column(
        width=90,
        spacing=10,
        data=view,
        controls=build_side_bar_controls(view, on_action),
    )

    return side_bar


def build_side_bar_controls(view: AppView, on_action: Callable[[str], Coroutine[Any, Any, None]]) -> list[ft.Control]:
    def build_button(section: dict) -> ft.Button:

        async def handle_click(e, action=section["action"]):
            await on_action(action)

        return ft.Button(
            content=section["label"],
            on_click=handle_click,
        )

    return [build_button(section) for section in SECTIONS.get(view, [])]
