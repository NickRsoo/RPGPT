from nicegui import ui
from ui import todo_rpg_app

def start_game(name):
    todo_rpg_app.ToDoRPGApp(name)  # Aufruf der korrekten Klasse in todo_rpg_app

with ui.column().classes("p-4"):
    ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
    name_input = ui.input("Charakternamen eingeben")
    ui.button("Spiel starten", on_click=lambda: start_game(name_input.value))

ui.run()
