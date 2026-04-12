import os
import flet as ft

from database.connection import init_db
from views.access_view import AccessLogView
from views.members_view import MembersView
from views.access_control_view import AccessControlView


def main(page: ft.Page):
    page.title = "Sports Club Management System"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1000
    page.window_height = 700
    page.padding = 0

    schema_path = os.path.join("database", "schema.sql")
    init_db(schema_path)

    # Content area
    content_area = ft.Container(expand=True)

    def change_view(index):
        views = [
            AccessControlView,  # this is the gate
            AccessLogView,       # this is the hisotry of entries , denieds... etc 
            MembersView
        ]

        content_area.content = views[index](page)
        page.update()

    # Navigation 
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=180,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.LOGIN,
                label="Gate",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.HISTORY,
                label="History",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PEOPLE_OUTLINED,
                selected_icon=ft.Icons.PEOPLE,
                label="Members",
            ),
        ],
        on_change=lambda e: change_view(e.control.selected_index),
    )

    layout = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            content_area,
        ],
        expand=True,
    )

    page.add(layout)

    change_view(0)


if __name__ == "__main__":
    ft.app(target=main)