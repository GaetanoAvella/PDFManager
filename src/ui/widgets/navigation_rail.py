import flet as ft


start_sections = [
    {"label": "Open file", "icon": ft.Icons.UPLOAD_FILE_OUTLINED, "icon_selected": ft.Icons.UPLOAD_FILE},
    {"label": "Merge", "icon": ft.Icons.MERGE_TYPE_OUTLINED, "icon_selected": ft.Icons.MERGE_TYPE},
]

with_file_sections = [
    {"label": "Edit", "icon": ft.Icons.REORDER_OUTLINED, "icon_selected": ft.Icons.REORDER},
    {"label": "Delete", "icon": ft.Icons.DELETE_OUTLINE, "icon_selected": ft.Icons.DELETE},
    {"label": "Save", "icon": ft.Icons.SAVE_OUTLINED, "icon_selected": ft.Icons.SAVE},
    {"label": "Close", "icon": ft.Icons.CLOSE_OUTLINED, "icon_selected": ft.Icons.CLOSE}
]

def build_navigation_rail(state: str, on_change_callback) -> ft.NavigationRail:
    nav_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=90,
        min_extended_width=180,
        bgcolor="#161b22",
        indicator_color="#238636",
        data=state,
        destinations=build_nav_destinations(state),
        on_change=on_change_callback,
    )

    return nav_rail

def build_nav_destinations(state: str) -> list[ft.NavigationRailDestination]:
    def build_destination(section) -> ft.NavigationRailDestination:
        return ft.NavigationRailDestination(
            label=section["label"],
            icon=section["icon"],
            selected_icon=section["icon_selected"],
        )

    destinations = []

    match state:
        case "START":
            for i in start_sections:
                destinations.append(build_destination(i))
        case "FILE_OPEN":
            for i in with_file_sections:
                destinations.append(build_destination(i))

    return destinations