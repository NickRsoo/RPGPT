# main.py
from nicegui import ui
from todo_rpg_app import ToDoRPGApp

def main():
    with ui.column().classes("p-4"):
        ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
        name_input = ui.input("Charakternamen eingeben")
        ui.button("Spiel starten", on_click=lambda: ToDoRPGApp(name_input.value))

ui.run()
