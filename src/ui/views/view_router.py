from typing import Callable, TYPE_CHECKING

from state import AppView
from . import build_edit_view
from .start_view import build_start_view
from .read_view import build_read_view

if TYPE_CHECKING:
    from ui.app_controller import AppController


def build_view(app_view: AppView) -> Callable[["AppController"], None]:
    match app_view:
        case AppView.START:
            return build_start_view
        case AppView.READ:
            return build_read_view
        case AppView.EDIT:
            return build_edit_view
        case _:
            return build_start_view