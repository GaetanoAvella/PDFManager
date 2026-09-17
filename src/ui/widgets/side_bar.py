import flet as ft
from state import AppView


SECTIONS: dict[AppView, list[dict]] = {
    AppView.EDIT: [
        {"label": "Select", "action": "select"},  #on/off
        {"label": "Delete", "action": "delete"},  #one-shot
        {"label": "Reset", "action": "reset"},  #one-shot
        {"label": "Save", "action": "save"},  #one-shot
        {"label": "Close", "action": "close"},  #one-shot
    ]
}


class SideBar():
    def __init__(self):
        self.control: ft.Column = ft.Column(
            width=90,
            spacing=10,
        )
        self.change_view_buttons: list[ft.Control] = []
        self.utilities: list[ft.Control] = []


    def refresh(self):
        self.control.controls.clear()

        for button in self.change_view_buttons:
            self.control.controls.append(button)

        if self.utilities:
            self.control.controls.append(ft.Container(expand=True))
            for utility in self.utilities:
                self.control.controls.append(utility)

        self.control.update()


    def add_change_view_button(self, button: ft.Control):
        if button not in self.change_view_buttons:
            self.change_view_buttons.append(button)


    def add_utility(self, utility: ft.Control):
        if utility not in self.utilities:
            self.utilities.append(utility)


    def clear(self):
        self.change_view_buttons.clear()
        self.utilities.clear()
        self.control.controls.clear()


"""def build_side_bar(view: AppView, on_action: Callable[[str], Coroutine[Any, Any, None]]) -> ft.Column:
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

    return [build_button(section) for section in SECTIONS.get(view, [])]"""
