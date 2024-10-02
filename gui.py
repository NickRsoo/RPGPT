from nicegui import ui
from database import create_connection, setup_database

def run_gui():
    conn = create_connection()

    # Beispiel für Benutzer- und Aufgabenverwaltung
    with ui.row():
        name_input = ui.input('Name')
        race_input = ui.input('Rasse')
        class_input = ui.input('Klasse')
        ui.button('Benutzer erstellen', on_click=lambda: add_user(name_input.value, race_input.value, class_input.value))

    # Beispiel für das Aufgabenformular
    with ui.row():
        title_input = ui.input('Aufgabe')
        due_date_input = ui.input('Fälligkeitsdatum')
        difficulty_input = ui.select(['leicht', 'mittel', 'schwer'], 'Schwierigkeit')
        ui.button('Aufgabe hinzufügen', on_click=lambda: add_quest(1, title_input.value, due_date_input.value, difficulty_input.value))

    # NiceGUI starten
    ui.run()
