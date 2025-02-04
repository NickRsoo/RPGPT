

# Rest des Spiels starten
from nicegui import ui
from ui import todo_rpg_app


from nicegui import ui
from ui import todo_rpg_app
import sqlite3
print(sqlite3.sqlite_version)


# Liste der Rassen mit ihren Attributen
RACES = [
    {"name": "Mensch", "bonus": "Ausgewogen"},
    {"name": "Ork", "bonus": "Stark, aber langsam"},
    {"name": "Elfe", "bonus": "Schnell, aber schwach"}
]


AVATARS = [
    {"name": "Avatar 1", "image": "C:/Github/RPGPT/app/assets/avatar/avatar1.png"},
    {"name": "Avatar 2", "image": "C:/Github/RPGPT/app/assets/avatar/avatar2.png"},
    {"name": "Avatar 3", "image": "C:/Github/RPGPT/app/assets/avatar/avatar3.png"},
]

def start_game(name,container):
    """Startet das Spiel mit Name, Rasse und Avatar."""
    if not name.strip():
        ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
        return
    container.clear()  # Entfernt Auswahl
    todo_rpg_app.ToDoRPGApp(name)  # Spiel starten

def handle_name_input(name, container):
    """Wechselt von der Namenseingabe zur Rassen-Auswahl."""
    if not name.strip():
        ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
        return
    container.clear()
    start_game(name, container)

# UI: Namenseingabe 
with ui.column().classes("p-4") as input_container:
    ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
    name_input = ui.input("Charakternamen eingeben").classes("mb-4")
    ui.button("Spiel starten", on_click=lambda: handle_name_input(name_input.value, input_container))
    
ui.run()
