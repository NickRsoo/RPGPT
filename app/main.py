from nicegui import ui
from ui import todo_rpg_app

def start_game(name, container):
    if not name.strip():
        ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
        return
    container.clear()  # Entfernt die Eingabe und den Button
    todo_rpg_app.ToDoRPGApp(name)  # Startet das Spiel

with ui.column().classes("p-4") as input_container:  # Container für die Eingabe
    ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
    name_input = ui.input("Charakternamen eingeben").classes("mb-4")
    ui.button("Spiel starten", on_click=lambda: start_game(name_input.value, input_container))

ui.run()
