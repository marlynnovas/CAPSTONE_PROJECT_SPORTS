import flet as ft
from services.payment_service import PaymentService
from services.membership_service import MembershipService
from datetime import datetime

def PaymentsView(page: ft.Page):
    def stat_card(title, val, sub, clr):
        return ft.Container(
            content=ft.Column([
                ft.Text(str(val), size=26, weight=ft.FontWeight.BOLD, color=clr),
                ft.Text(title, size=12, weight=ft.FontWeight.BOLD),
                ft.Text(sub,   size=11, color=ft.Colors.ON_SURFACE_VARIANT),
            ], spacing=2),
            bgcolor=ft.Colors.SURFACE_CONTAINER, border_radius=12, padding=16, expand=True
        )
