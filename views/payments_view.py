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

    def make_stats():
        rev     = PaymentService.revenue_mtd()
        pending = PaymentService.count_by_status("pending")
        overdue = PaymentService.count_by_status("failed")
        avg     = PaymentService.average_amount()
        count   = PaymentService.count_this_month()
        return ft.Row([
            stat_card("Revenue (MTD)",  f"${rev:,.0f}",  "Completed only",   ft.Colors.GREEN),
            stat_card("Pending",        pending,          "Awaiting payment",  ft.Colors.ORANGE),
            stat_card("Failed",         overdue,          "Needs attention",   ft.Colors.RED),
            stat_card("Avg Ticket",     f"${avg:,.0f}",  "Per transaction",   ft.Colors.BLUE),
            stat_card("Transactions",   count,            "This month",        ft.Colors.PURPLE),
        ], spacing=12)