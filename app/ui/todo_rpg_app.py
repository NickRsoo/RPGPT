# todo_rpg_app.py
from nicegui import ui
from components import character
from components import quest
from components import shop

class ToDoRPGApp:
    def __init__(self, character_name):
        self.character = character(character_name)
        self.quests = []
        self.shop = shop()
        self.setup_ui()

    def setup_ui(self):
        # Header und Charakterstatus
        ui.label(f"Willkommen, {self.character.name}!").classes("text-2xl")
        with ui.row().classes('justify-between'):
            self.status = ui.label(self.get_status()).classes("text-lg")
            ui.button("Status aktualisieren", on_click=self.update_status)

        # Quests
        ui.label("Quests").classes("text-xl mt-4")
        self.quest_list = ui.column()
        ui.button("Neue Quest hinzufügen", on_click=self.add_quest_dialog)

        # Shop
        ui.label("Shop").classes("text-xl mt-4")
        self.shop_items = ui.column()
        self.display_shop()

    def add_quest_dialog(self):
        with ui.dialog() as dialog, ui.card():
            ui.label("Neue Quest hinzufügen").classes("text-lg")
            description = ui.input("Questbeschreibung")
            xp_reward = ui.number("XP-Belohnung")
            gold_reward = ui.number("Gold-Belohnung")
            ui.button("Hinzufügen", on_click=lambda: self.add_quest(description.value, int(xp_reward.value), int(gold_reward.value), dialog))

    def add_quest(self, description, xp_reward, gold_reward, dialog=None):
        quest = quest(description, xp_reward, gold_reward)
        self.quests.append(quest)
        with self.quest_list:
            ui.row().classes('items-center mt-2').with_(
                ui.label(f"{description} - Belohnung: {xp_reward} XP, {gold_reward} Gold").classes("text-base"),
                ui.button("Abschließen", on_click=lambda: self.complete_quest(quest))
            )
        if dialog:
            dialog.close()

    def complete_quest(self, quest):
        if quest.complete(self.character):
            self.update_status()

    def display_shop(self):
        for item_name, item_info in self.shop.items.items():
            with self.shop_items:
                ui.row().classes('items-center mt-2').with_(
                    ui.label(f"{item_name}: {item_info['cost']} Gold").classes("text-base"),
                    ui.button(f"Kaufen ({item_name})", on_click=lambda name=item_name: self.shop.buy(self.character, name))
                )

    def update_status(self):
        self.status.set_text(self.get_status())

    def get_status(self):
        achievements = ", ".join(self.character.achievements) if self.character.achievements else "Keine"
        return f"Level: {self.character.level}, XP: {self.character.xp}/{self.character.level * 100}, Gold: {self.character.gold}, Achievements: {achievements}"
