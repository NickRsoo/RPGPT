from nicegui import ui
from ui import todo_rpg_app

# Liste von verfügbaren Avataren
AVATARS = [
    {"name": "Avatar 1", "image": "C:/Github/RPGPT/app/assets/Avatar/avatar1.png"},
    {"name": "Avatar 2", "image": "C:/Github/RPGPT/app/assets/Avatar/avatar2.png"},
    {"name": "Avatar 3", "image": "C:/Github/RPGPT/app/assets/Avatar/avatar3.png"},
]

def start_game(name, container):
    """
    Startet die Avatar-Auswahl nach der Namenseingabe.
    """
    if not name.strip():
        ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
        return
    container.clear()  # Entfernt die Eingabe und den Button
    show_avatar_selection(name, container)

def show_avatar_selection(name, container):
    """
    Zeigt die Avatar-Auswahl.
    """
    ui.label(f"Willkommen, {name}! Wähle deinen Avatar:").classes("text-xl mb-4", parent=container)
    
    # Anzeige der verfügbaren Avatare
    with container:
        for avatar in AVATARS:
            with ui.card().classes("w-1/3 inline-block p-4"):
                ui.image(avatar["image"]).style("width: 100px; height: 100px; border-radius: 50%;")
                ui.button("Auswählen", on_click=lambda a=avatar: select_avatar(name, a, container)).classes("mt-2 bg-blue-500 text-white rounded")

def select_avatar(name, avatar, container):
    """
    Speichert den ausgewählten Avatar und startet das Spiel.
    """
    container.clear()  # Entfernt die Avatar-Auswahl
    todo_rpg_app.ToDoRPGApp(name, avatar)  # Startet das Spiel mit dem Avatar

with ui.column().classes("p-4") as input_container:
    ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
    name_input = ui.input("Charakternamen eingeben").classes("mb-4")
    ui.button("Spiel starten", on_click=lambda: start_game(name_input.value, input_container))

ui.run(static_files={'/assets': 'assets'})
