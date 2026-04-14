import os
import flet as ft

from database.connection import init_db
from views.access_view import AccessLogView
from views.members_view import MembersView
from views.access_control_view import AccessControlView
from views.reports_view import ReportsView
from views.plans_view import PlansView
from views.payments_view import PaymentsView
from views.access_view import AccessLogView


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
            AccessControlView,# this is the gate 
            AccessLogView,# this is the hisotry of entries , denieds... etc 
            MembersView,
                   
            
        ]

        content_area.content = views[index](page)
        page.update()

    # Navigation 
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=180,
        bgcolor=ft.Colors.BLACK,
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
            ft.NavigationRailDestination(
                icon=ft.Icons.INSERT_CHART_OUTLINED,
                selected_icon=ft.Icons.INSERT_CHART,
                label="Reports",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.LIST_ALT_OUTLINED,
                selected_icon=ft.Icons.LIST_ALT,
                label="Plans",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PAYMENTS_OUTLINED,
                selected_icon=ft.Icons.PAYMENTS,
                label="Payments",
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