import flet as ft
from services.access_service import AccessService
from services.member_service import MemberService
from database.connection import get_connection

def AccessControlView(page: ft.Page):

    status_banner = ft.Container(
        content=ft.Column([
            ft.Icon(ft.Icons.LOCK, size=64, color=ft.Colors.GREY_400),
            ft.Text("Waiting for validation...", size=18, color=ft.Colors.ON_SURFACE_VARIANT)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=40, border_radius=15, bgcolor=ft.Colors.SURFACE_CONTAINER, 
        width=500, alignment=ft.Alignment(0, 0)
    )

    member_id_field = ft.TextField(
        label="Enter Member ID", 
        width=300, 
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=lambda e: validate_access(e)
    )

    def validate_access(e):
        if not member_id_field.value:
            return
        
        mid = int(member_id_field.value)
      
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.first_name || ' ' || m.last_name as full_name, 
                   ms.status, ms.end_date, p.name as plan_name
            FROM members m
            LEFT JOIN memberships ms ON m.id = ms.member_id
            LEFT JOIN plans p ON ms.plan_id = p.id
            WHERE m.id = ?
            ORDER BY ms.id DESC LIMIT 1
        """, (mid,))
        row = cursor.fetchone()
        conn.close()

    def update_banner(success, message, icon, color):
        status_banner.bgcolor = ft.Colors.GREEN_400 if success else ft.Colors.RED_400
        status_banner.content = ft.Column([
            ft.Icon(icon, size=80, color=ft.Colors.WHITE),
            ft.Text(message, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text("Valid as of today" if success else "Contact support", color=ft.Colors.WHITE70)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()
