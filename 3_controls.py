import flet as ft 

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.add(t)
    #page.controls.append(t)
    page.update()

ft.app(target=main)