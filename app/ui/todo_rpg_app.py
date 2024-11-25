from nicegui import ui
from components.character import Character
from components.quest import Quest
from components.shop import Shop

class ToDoRPGApp:
    def __init__(self, character_name):
        self.character = Character(character_name)
        self.quests = []
        self.shop = Shop()
        self.setup_ui()

    def setup_ui(self):
        ui.label(f"Willkommen, {self.character.name}!").classes("text-2xl")

        with ui.row().classes('justify-between'):
            self.status = ui.label(self.get_status()).classes("text-lg")
            ui.button("Status aktualisieren", on_click=self.update_status)

        ui.label("Quests").classes("text-xl mt-4")
        with ui.column() as self.quest_list:
            pass

        ui.button("Neue Quest hinzufügen", on_click=self.add_quest_dialog)

        ui.label("Shop").classes("text-xl mt-4")
        with ui.column() as self.shop_items:
            self.display_shop()

        ui.label("Gekaufte Items").classes("text-xl mt-4")
        with ui.column() as self.item_list:  # Initialisiert den Item-Bereich
            self.display_items()




    def add_quest_dialog(self):
        dialog = ui.dialog()
        with dialog:
            with ui.card():
                ui.label("Neue Quest hinzufügen").classes("text-lg")
                description = ui.input("Questbeschreibung")
                xp_reward = ui.number("XP-Belohnung", value=0, min=0)
                gold_reward = ui.number("Gold-Belohnung", value=0, min=0)
                ui.button(
                    "Hinzufügen",
                    on_click=lambda: self.add_quest(
                        description.value,
                        int(xp_reward.value),
                        int(gold_reward.value),
                        dialog
                    )
                )
        dialog.open()

    def add_quest(self, description, xp_reward, gold_reward, dialog=None):
        if not description.strip():
            ui.notify("Die Beschreibung darf nicht leer sein.", color="red")
            return
        quest = Quest(description, xp_reward, gold_reward)
        self.quests.append(quest)  # Quest zur internen Liste hinzufügen
        self.display_quest(quest)  # Quest zur Benutzeroberfläche hinzufügen
        if dialog:
            dialog.close()
        ui.notify(f"Quest '{description}' hinzugefügt!", color="green")


    def display_quest(self, quest):
        """
        Fügt eine Quest zur Benutzeroberfläche hinzu.
        """
        with self.quest_list:  # Stellt sicher, dass die Quest in der Liste angezeigt wird
            row = ui.row().classes('items-center mt-2')
            ui.label(f"{quest.description} - Belohnung: {quest.xp_reward} XP, {quest.gold_reward} Gold").classes("text-base")
            ui.button("Abschließen", on_click=lambda q=quest: self.complete_quest(q))



    def complete_quest(self, quest):
        if quest.complete(self.character):
            self.update_status()
            ui.notify(f"Quest '{quest.description}' abgeschlossen!", color="green")
        else:
            ui.notify("Quest konnte nicht abgeschlossen werden.", color="red")

    def display_shop(self):
    # Entfernen Sie alte Shop-Items
        self.shop_items.clear()
    
        for item_name, item_info in self.shop.items.items():
            with ui.row().classes('items-center mt-2'):  # Keine 'parent'-Parameter
                ui.label(f"{item_name}: {item_info['cost']} Gold").classes("text-base")
                ui.button(
                    f"Kaufen ({item_name})",
                    on_click=lambda name=item_name: self.buy_item(name)
                )



    def buy_item(self, item_name):
        """
        Führt den Kauf eines Items aus und aktualisiert den Item-Bereich.
        """
        if self.shop.buy(self.character, item_name):
            item_info = self.shop.items[item_name]
            self.character.add_item(item_name, item_info)
            self.update_status()
            self.display_items()  # Aktualisiert den Item-Bereich
            ui.notify(f"'{item_name}' erfolgreich gekauft!", color="green")
        else:
            ui.notify(f"Nicht genügend Gold für '{item_name}'.", color="red")

    def update_status(self):
        self.status.set_text(self.get_status())

    def get_status(self):
        achievements = ", ".join(self.character.achievements) if self.character.achievements else "Keine"
        return (
            f"Level: {self.character.level}, "
            f"XP: {self.character.xp}/{self.character.level * 100}, "
            f"Gold: {self.character.gold}, "
            f"Achievements: {achievements}"
        )
    
    def display_items(self):
        """
        Zeigt alle gekauften Items im Bereich 'Gekaufte Items' an.
        """
        self.item_list.clear()
        for item_name, item_info in self.character.items.items():
            with self.item_list:
                with ui.row().classes('items-center mt-2'):
                    # Lokales Icon wird als Bild geladen
                    ui.image(item_info['icon']).style('width: 50px; height: 50px;')
                    ui.label(f"{item_name}: {item_info['description']}").classes("text-base")




# Sicherstellen, dass die Anwendung korrekt gestartet wird
if __name__ == "__main__":
    app = ToDoRPGApp("Abenteurer")
    ui.run(static_files={'/assets': 'assets'})
