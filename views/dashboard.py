import flet as ft
from services.member_service import MemberService
from services.access_service import AccessService

first_name_input = ft.TextField(label="First Name")
last_name_input  = ft.TextField(label="Last Name")
email_input      = ft.TextField(label="Email")

def save_member(e):
        mid = MemberService.create_member(first_name_input.value, last_name_input.value, email_input.value, "")
        if mid:
            page.snack_bar = ft.SnackBar(ft.Text(f"Member #{mid} created!"), bgcolor=ft.Colors.GREEN)
            page.snack_bar.open = True
            new_member_dialog.open = False
            page.update()


new_member_dialog = ft.AlertDialog(
        title=ft.Text("Quick Register Member"),
        content=ft.Column([first_name_input, last_name_input, email_input], tight=True),
        actions=[ft.TextButton("Cancel", on_click=lambda _: setattr(new_member_dialog, "open", False)), 
                 ft.ElevatedButton("Create", on_click=save_member)]


membership_dropdown = ft.Dropdown(label="Select Membership", options=[])
payment_amount = ft.TextField(label="Amount ($)", keyboard_type=ft.KeyboardType.NUMBER)