import flet as ft
from services.access_service import AccessService

def AccessLogView(page: ft.Page):

    
    def mini_stat(title, val, clr):
        return ft.Container(
            content=ft.Column([
                ft.Text(str(val), size=24, weight=ft.FontWeight.BOLD, color=clr),
                ft.Text(title, size=12, color=ft.Colors.ON_SURFACE_VARIANT),
            ], spacing=2),
            bgcolor=ft.Colors.SURFACE_CONTAINER, border_radius=10, padding=16, expand=True
        )

    def make_stats():
        today   = AccessService.count_today()
        granted = AccessService.count_granted_today()
        denied  = AccessService.count_denied_today()
        active  = AccessService.count_active_now()
        peak    = AccessService.peak_hour_today()
        return ft.Row([
            mini_stat("Total Today",  today,   ft.Colors.BLUE),
            mini_stat("Granted",      granted, ft.Colors.GREEN),
            mini_stat("Denied",       denied,  ft.Colors.RED),
            mini_stat("Active Now",   active,  ft.Colors.PURPLE),
            mini_stat("Peak Hour",    peak,    ft.Colors.ORANGE),
        ], spacing=12)

    stats_container = ft.Container(content=make_stats())