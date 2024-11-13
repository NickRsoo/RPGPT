# main.py
from nicegui import ui
from todo_rpg_app import ToDoRPGApp

def main():
    ui.label("RPG To-Do List App mit NiceGUI")
    name = ui.input("Charakternamen eingeben")
    ui.button("Spiel starten", on_click=lambda: ToDoRPGApp(name.value))

ui.run()
