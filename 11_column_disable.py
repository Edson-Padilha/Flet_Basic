import flet as ft 

def main(page: ft.Page):
    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disable = True
    page.add(c)
ft.app(target=main)