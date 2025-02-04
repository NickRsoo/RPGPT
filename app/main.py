#from nicegui import ui
#from ui import todo_rpg_app"

# #def start_game(name, container):
#     if not name.strip():
#         ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
#         return
#     container.clear()  # Entfernt die Eingabe und den Button
#     todo_rpg_app.ToDoRPGApp(name)  # Startet das Spiel

# with ui.column().classes("p-4") as input_container:  # Container für die Eingabe
#     ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
#     name_input = ui.input("Charakternamen eingeben").classes("mb-4")
#     ui.button("Spiel starten", on_click=lambda: start_game(name_input.value, input_container))

# ui.run()


# from nicegui import ui
# from ui import todo_rpg_app

# # Liste der Rassen mit ihren Attributen
# RACES = [
#     {"name": "Mensch", "bonus": "Ausgewogen"},
#     {"name": "Ork", "bonus": "Stark, aber langsam"},
#     {"name": "Elfe", "bonus": "Schnell, aber schwach"}
# ]

# # Liste von Avataren
# AVATARS = [
#     {"name": "Avatar 1", "image": "C:/Github/RPGPT/app/assets/avatar/avatar1.png"},
#     {"name": "Avatar 2", "image": "C:/Github/RPGPT/app/assets/avatar/avatar2.png"},
#     {"name": "Avatar 3", "image": "C:/Github/RPGPT/app/assets/avatar/avatar3.png"},
# ]

# def start_game(name, race, avatar, container):
#     """Startet das Spiel mit Name, Rasse und Avatar."""
#     if not name.strip():
#         ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
#         return
#     container.clear()  # Entfernt Auswahl
#     todo_rpg_app.ToDoRPGApp(name, race, avatar)  # Spiel starten

# def show_avatar_selection(name, race, container):
#     """Zeigt die Avatar-Auswahl nach der Rassen-Wahl."""
#     container.clear()
#     ui.label(f"Willkommen {name} ({race})! Wähle einen Avatar:").classes("text-xl mb-4")
    
#     with container:
#         for avatar in AVATARS:
#             with ui.card().classes("w-1/3 inline-block p-4"):
#                 ui.image(avatar["image"]).style("width: 100px; height: 100px; border-radius: 50%;")
#                 ui.button("Auswählen", on_click=lambda a=avatar: start_game(name, race, a, container)).classes("mt-2 bg-blue-500 text-white rounded")

# def show_race_selection(name, container):
#     """Zeigt die Rassen-Auswahl nach der Namenseingabe."""
#     container.clear()
#     ui.label(f"Hallo {name}, wähle deine Rasse:").classes("text-xl mb-4")
    
#     with container:
#         for race in RACES:
#             with ui.card().classes("w-1/3 inline-block p-4"):
#                 ui.label(f"{race['name']}").classes("text-lg font-bold")
#                 ui.label(f"Bonus: {race['bonus']}").classes("text-sm text-gray-500")
#                 ui.button("Auswählen", on_click=lambda r=race["name"]: show_avatar_selection(name, r, container)).classes("mt-2 bg-green-500 text-white rounded")

# def handle_name_input(name, container):
#     """Wechselt von der Namenseingabe zur Rassen-Auswahl."""
#     if not name.strip():
#         ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
#         return
#     container.clear()
#     show_race_selection(name, container)

# # UI: Namenseingabe → Rassenwahl → Avatarwahl
# with ui.column().classes("p-4") as input_container:
#     ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
#     name_input = ui.input("Charakternamen eingeben").classes("mb-4")
#     ui.button("Spiel starten", on_click=lambda: handle_name_input(name_input.value, input_container))

# ui.run()

from nicegui import ui
from ui import todo_rpg_app

# Liste der Rassen mit ihren Attributen
RACES = [
    {"name": "Mensch", "bonus": "Ausgewogen"},
    {"name": "Ork", "bonus": "Stark, aber langsam"},
    {"name": "Elfe", "bonus": "Schnell, aber schwach"}
]

# Liste von Avataren
AVATARS = [
    {"name": "Avatar 1", "image": "C:/Github/RPGPT/app/assets/avatar/avatar1.png"},
    {"name": "Avatar 2", "image": "C:/Github/RPGPT/app/assets/avatar/avatar2.png"},
    {"name": "Avatar 3", "image": "C:/Github/RPGPT/app/assets/avatar/avatar3.png"},
]

def start_game(name, race, avatar, container):
    """Startet das Spiel mit Name, Rasse und Avatar."""
    if not name.strip():
        ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
        return
    container.clear()  # Entfernt Auswahl
    todo_rpg_app.ToDoRPGApp(name, race, avatar)  # Spiel starten

def show_avatar_selection(name, race, container):
    """Zeigt die Avatar-Auswahl nach der Rassen-Wahl."""
    container.clear()
    ui.label(f"Willkommen {name} ({race})! Wähle einen Avatar:").classes("text-xl mb-4")
    
    with container:
        for avatar in AVATARS:
            with ui.card().classes("w-1/3 inline-block p-4"):
                ui.image(avatar["image"]).style("width: 100px; height: 100px; border-radius: 50%;")
                ui.button(
                    "Auswählen",
                    on_click=lambda a=avatar: start_game(name, race, a, container)
                ).classes("mt-2 bg-blue-500 text-white rounded")

def show_race_selection(name, container):
    """Zeigt die Rassen-Auswahl nach der Namenseingabe."""
    container.clear()
    ui.label(f"Hallo {name}, wähle deine Rasse:").classes("text-xl mb-4")
    
    with container:
        for race in RACES:
            with ui.card().classes("w-1/3 inline-block p-4"):
                ui.label(f"{race['name']}").classes("text-lg font-bold")
                ui.label(f"Bonus: {race['bonus']}").classes("text-sm text-gray-500")
                ui.button(
                    "Auswählen",
                    on_click=lambda r=race["name"]: show_avatar_selection(name, r, container)
                ).classes("mt-2 bg-green-500 text-white rounded")

def handle_name_input(name, container):
    """Wechselt von der Namenseingabe zur Rassen-Auswahl."""
    if not name.strip():
        ui.notify("Bitte einen gültigen Namen eingeben!", color="red")
        return
    container.clear()
    show_race_selection(name, container)

# UI: Namenseingabe → Rassenwahl → Avatarwahl
with ui.column().classes("p-4") as input_container:
    ui.label("RPG To-Do List App mit NiceGUI").classes("text-2xl mb-4")
    name_input = ui.input("Charakternamen eingeben").classes("mb-4")
    ui.button("Spiel starten", on_click=lambda: handle_name_input(name_input.value, input_container))

ui.run()
