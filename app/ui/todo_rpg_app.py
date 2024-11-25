from nicegui import ui
from components.character import Character
from components.shop import Shop
from components.bosses import Boss

class ToDoRPGApp:
    def __init__(self, character_name):
        self.character = Character(character_name)
        self.shop = Shop()
        self.bosses = self.create_bosses()
        self.quests = []
        self.completed_quests = []
        self.setup_ui()

    def create_bosses(self):
        """
        Erstellt die Liste der Bosse mit Levelanforderungen und Belohnungen.
        """
        return [
            Boss("Goblin King", 1, 30, 5, 10),
            Boss("Skeleton Warrior", 2, 50, 7, 20),
            Boss("Orc Chieftain", 3, 70, 10, 30),
            Boss("Dark Mage", 4, 90, 12, 50),
            Boss("Forest Guardian", 5, 110, 15, 70),
            Boss("Shadow Assassin", 6, 130, 18, 100),
            Boss("Fire Elemental", 7, 150, 20, 150),
            Boss("Ice Dragon", 8, 200, 25, 200),
            Boss("Demon Lord", 9, 250, 30, 300),
            Boss("Eternal Titan", 10, 300, 35, 500),
        ]

    def setup_ui(self):
        with ui.row().classes('h-screen'):
            # Navigation
            with ui.column().classes('bg-gray-800 text-white w-1/4 p-4'):
                ui.label("Menu").classes("text-xl font-bold mb-4")
                self.create_nav_button("Taverne", icon="local_bar", section="tavern")
                self.create_nav_button("Fights", icon="swords", section="fights")
                self.create_nav_button("Händler", icon="shopping_cart", section="shop")
                self.create_nav_button("Quarter", icon="house", section="character")
                self.create_nav_button("Achievements", icon="emoji_events", section="achievements")

            # Hauptbereich
            with ui.column().classes('w-3/4 p-4'):
                with ui.row().classes('justify-between items-center bg-gray-100 p-2 rounded mb-4'):
                    self.status = ui.label(self.get_status()).classes("text-lg")
                    ui.button("Status aktualisieren", on_click=self.update_status)

                self.main_content = ui.column().classes('w-full')
                self.display_tavern()

    def create_nav_button(self, label, icon=None, section=None):
        ui.button(label, icon=icon, on_click=lambda: self.change_content(section)).classes(
            "w-full text-left bg-gray-700 hover:bg-gray-600 text-white mb-2 p-2 rounded"
        )

    def change_content(self, section):
        self.main_content.clear()
        if section == "tavern":
            self.display_tavern()
        elif section == "fights":
            self.display_fights()
        elif section == "shop":
            self.display_shop()
        elif section == "character":
            self.display_character()
        elif section == "achievements":
            self.display_achievements()

    def display_tavern(self):
        """
        Zeigt die Taverne mit Quest-Optionen.
        """
        with self.main_content:
            ui.label("Taverne").classes("text-xl font-bold mb-4")

            # Aktive Quests
            ui.label("Aktive Quests").classes("text-lg font-bold mt-2")
            with ui.column().classes('gap-2'):
                for quest in self.quests:
                    with ui.row().classes('items-center gap-4'):
                        ui.label(f"{quest['name']} - {quest['description']}")
                        ui.button("Abschließen", on_click=lambda q=quest: self.complete_quest(q))

            # Fertige Quests
            ui.label("Fertige Quests").classes("text-lg font-bold mt-4")
            with ui.column().classes('gap-2'):
                for quest in self.completed_quests:
                    ui.label(f"{quest['name']}").classes("text-base text-green-600")

            # Neue Quest hinzufügen
            ui.label("Neue Quest hinzufügen").classes("text-lg font-bold mt-4")
            with ui.row().classes('gap-2 mt-2'):
                name_input = ui.input("Questname").classes("w-1/2")
                description_input = ui.input("Beschreibung").classes("w-1/2")
                ui.button("Hinzufügen", on_click=lambda: self.add_quest(name_input.value, description_input.value))

    def add_quest(self, name, description):
        """
        Fügt eine neue Quest zur Liste hinzu.
        """
        if not name.strip() or not description.strip():
            ui.notify("Questname und Beschreibung dürfen nicht leer sein.", color="red")
            return
        self.quests.append({"name": name, "description": description})
        ui.notify(f"Quest '{name}' hinzugefügt!", color="green")
        self.display_tavern()

    def complete_quest(self, quest):
        """
        Schließt eine Quest ab und verschiebt sie zu den fertigen Quests.
        """
        self.quests.remove(quest)
        self.completed_quests.append(quest)
        ui.notify(f"Quest '{quest['name']}' abgeschlossen!", color="green")
        self.display_tavern()

    def display_fights(self):
        """
        Zeigt die Liste der Bosse an, die freigeschaltet oder gesperrt sind.
        """
        with self.main_content:
            ui.label("Boss-Auswahl").classes("text-xl font-bold mb-4")
            with ui.column().classes('gap-4'):
                for boss in self.bosses:
                    with ui.card().classes('p-4'):
                        if self.character.level >= boss.level_required:
                            ui.label(f"{boss.name} (Level {boss.level_required}) - HP: {boss.hp}").classes("text-lg")
                            if not boss.defeated:
                                ui.button("Kämpfen", on_click=lambda b=boss: self.start_fight(b)).classes("mt-2 bg-green-500 hover:bg-green-400 text-white")
                            else:
                                ui.label("Besiegt").classes("text-green-500 text-lg mt-2")
                        else:
                            ui.label(f"{boss.name} (Level {boss.level_required})").classes("text-lg text-gray-500")
                            ui.label("Gesperrt").classes("text-gray-500 text-lg mt-2")

    def display_shop(self):
        with self.main_content:
            ui.label("Händler").classes("text-xl font-bold mb-2")
            for item_name, item_info in self.shop.items.items():
                with ui.row().classes('items-center gap-4'):
                    ui.label(f"{item_name}: {item_info['cost']} Gold")
                    ui.button(f"Kaufen", on_click=lambda name=item_name: self.buy_item(name))

    def display_character(self):
        with self.main_content:
            ui.label("Charakterinformationen").classes("text-xl font-bold mb-2")
            ui.label(f"Level: {self.character.level}")
            ui.label(f"Gold: {self.character.gold}")

    def display_achievements(self):
        with self.main_content:
            ui.label("Errungenschaften").classes("text-xl font-bold mb-2")
            if self.character.achievements:
                for achievement in self.character.achievements:
                    ui.label(f"- {achievement}")
            else:
                ui.label("Keine Errungenschaften.")

    def update_status(self):
        self.status.set_text(self.get_status())

    def get_status(self):
        return f"Level: {self.character.level}, Gold: {self.character.gold}"

if __name__ == "__main__":
    app = ToDoRPGApp("Abenteurer")
    ui.run(static_files={'/assets': 'assets'})
