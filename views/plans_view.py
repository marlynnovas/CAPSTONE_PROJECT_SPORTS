import flet as ft
from services.plan_service import PlanService

def PlansView(page: ft.Page):
    # Header
    header = ft.Row([
        ft.Column([
            ft.Text("Membership Plans", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Manage and create subscription plans for the club", 
                    color=ft.Colors.ON_SURFACE_VARIANT)
        ], expand=True),
        ft.ElevatedButton("Create New Plan", icon=ft.Icons.ADD, 
                          bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                          on_click=lambda _: open_add_dialog())
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
    edit_mode = False
    current_plan_id = None

    # dialogs
    dialog_title = ft.Text("Plan")
    name_input     = ft.TextField(label="Plan Name")
    price_input    = ft.TextField(label="Price ($)", keyboard_type=ft.KeyboardType.NUMBER)
    months_input   = ft.TextField(label="Duration (months)", keyboard_type=ft.KeyboardType.NUMBER)
    desc_input     = ft.TextField(label="Description", multiline=True)

    def open_add_dialog():
        nonlocal edit_mode
        edit_mode = False
        dialog_title.value = "Add New Plan"
        name_input.value = ""
        price_input.value = ""
        months_input.value = ""
        desc_input.value = ""
        dialog.open = True
        page.update()

    def open_edit_dialog(p):
        nonlocal edit_mode, current_plan_id
        edit_mode = True
        current_plan_id = p["id"]
        dialog_title.value = f"Edit Plan #{p['id']}"
        name_input.value = p["name"]
        price_input.value = str(p["price"])
        months_input.value = str(p["duration_months"])
        desc_input.value = p["description"] or ""
        dialog.open = True
        page.update()

    def save_plan(e):
        nonlocal edit_mode, current_plan_id
        if not name_input.value or not price_input.value: return
        
        try:
            price = float(price_input.value)
            mos = int(months_input.value)
        except: return

        if edit_mode:
            PlanService.update_plan(current_plan_id, name_input.value, price, mos, desc_input.value)
        else:
            PlanService.create_plan(name_input.value, price, mos, desc_input.value)
            
        dialog.open = False
        refresh_table()
        page.update()

    dialog = ft.AlertDialog(
        title=dialog_title,
        content=ft.Column([name_input, price_input, months_input, desc_input], tight=True),
        actions=[
            ft.TextButton("Cancel", on_click=lambda _: setattr(dialog, "open", False)),
            ft.ElevatedButton("Save", on_click=save_plan)
        ]
    )
    page.overlay.append(dialog)