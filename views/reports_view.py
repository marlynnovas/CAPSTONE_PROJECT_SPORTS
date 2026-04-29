import flet as ft
from database.connection import get_connection
from services.member_service import MemberService
from services.payment_service import PaymentService
from services.access_service import AccessService
from datetime import datetime

def ReportsView(page: ft.Page):

    def make_stats_row():
        total, active, revenue = (
            MemberService.count_members(),
            MemberService.count_by_status("active"),
            PaymentService.revenue_mtd()
        )
        return ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text(str(total), size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Total Members")
                ]),
                expand=True,
                bgcolor=ft.Colors.SURFACE_CONTAINER,
                padding=20,
                border_radius=12
            ),
            ft.Container(
                ft.Column([
                    ft.Text(
                        str(active),
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN
                    ),
                    ft.Text("Active Accounts")
                ]),
                expand=True,
                bgcolor=ft.Colors.SURFACE_CONTAINER,
                padding=20,
                border_radius=12
            ),
            ft.Container(
                ft.Column([
                    ft.Text(
                        f"${revenue:,.0f}",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PURPLE
                    ),
                    ft.Text("Revenue MTD")
                ]),
                expand=True,
                bgcolor=ft.Colors.SURFACE_CONTAINER,
                padding=20,
                border_radius=12
            ),
        ], spacing=12)

    def get_denied_table():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM denied_access_summary")
        rows = cursor.fetchall()
        conn.close()

        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Member")),
                ft.DataColumn(ft.Text("Denied Access Count")),
                ft.DataColumn(ft.Text("Last Attempt"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(r[0])),
                        ft.DataCell(
                            ft.Text(
                                str(r[1]),
                                color=ft.Colors.RED
                            )
                        ),
                        ft.DataCell(ft.Text(str(r[2])))
                    ]
                )
                for r in rows
            ],
            expand=True
        )

    return ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text(
                        "System Reports",
                        size=32,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        f"Reports generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                        color=ft.Colors.ON_SURFACE_VARIANT
                    )
                ], expand=True),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),

            make_stats_row(),

            ft.Text(
                "Access Issues Summary",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            ft.Container(
                content=ft.Column(
                    [get_denied_table()],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True
                ),
                bgcolor=ft.Colors.BLACK,
                border_radius=12,
                padding=15,
                expand=True
            ),
        ],
            spacing=16,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        ),
        padding=28,
        expand=True
    )