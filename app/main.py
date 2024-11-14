# main.py
from nicegui import ui
from ui import todo_rpg_app
todo_rpg_app=todo_rpg_app.ToDoRPGApp()

with ui.column().classes("p-4"):
    ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
    name_input = ui.input("Charakternamen eingeben")
    ui.button("Spiel starten", on_click=lambda: todo_rpg_app(name_input.value))

ui.run()
