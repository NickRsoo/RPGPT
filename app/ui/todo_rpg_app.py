from nicegui import ui
from components.character import Character
from components.shop import Shop
from components.bosses import Boss
from components.quest import Quest  # Import der Quest-Klasse

class ToDoRPGApp:
    def __init__(self, character_name):
        self.character = Character(character_name)
        self.shop = Shop()
        self.bosses = self.create_bosses()
        self.quests = []  # Liste für aktive Quests
        self.completed_quests = []  # Liste für abgeschlossene Quests
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
                        ui.label(f"{quest.description} - {quest.xp_reward} XP, {quest.gold_reward} Gold")
                        ui.button("Abschließen", on_click=lambda q=quest: self.complete_quest(q))

            # Fertige Quests
            ui.label("Fertige Quests").classes("text-lg font-bold mt-4")
            with ui.column().classes('gap-2'):
                for quest in self.completed_quests:
                    ui.label(f"{quest.description}").classes("text-base text-green-600")

            # Neue Quest hinzufügen
            ui.label("Neue Quest hinzufügen").classes("text-lg font-bold mt-4")
            with ui.row().classes('gap-2 mt-2'):
                description_input = ui.input("Beschreibung").classes("w-1/2")
                xp_input = ui.number("XP-Belohnung", value=10, min=1).classes("w-1/4")
                gold_input = ui.number("Gold-Belohnung", value=10, min=1).classes("w-1/4")
                ui.button("Hinzufügen", on_click=lambda: self.add_quest(description_input.value, xp_input.value, gold_input.value))

    def add_quest(self, description, xp_reward, gold_reward):
        """
        Fügt eine neue Quest zur Liste hinzu.
        """
        if not description.strip():
            ui.notify("Beschreibung darf nicht leer sein.", color="red")
            return
        quest = Quest(description, xp_reward, gold_reward)
        self.quests.append(quest)
        ui.notify(f"Quest '{description}' hinzugefügt!", color="green")
        self.display_tavern()

    def complete_quest(self, quest):
        """
        Schließt eine Quest ab und verschiebt sie zu den fertigen Quests.
        """
        if quest.complete(self.character):
            self.quests.remove(quest)
            self.completed_quests.append(quest)
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
        """
        Zeigt die verfügbaren Shop-Items mit Bildern und ermöglicht das Kaufen.
        """
        with self.main_content:
            ui.label("Händler").classes("text-xl font-bold mb-4")
            for item_name, item_info in self.shop.items.items():
                with ui.row().classes('items-center gap-4'):
                    # Bild des Items
                    ui.image(item_info["image"]).style("width: 50px; height: 50px;")
                    
                    # Item-Details
                    ui.label(f"{item_name}: {item_info['cost']} Gold")
                    
                    # Kaufen-Button
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
    
    def start_fight(self, boss):
        """
        Rundenbasierter Kampf gegen einen Boss.
        """
        player_turn = True  # Der Spieler beginnt
        boss_hp = boss.hp
        player_hp = self.character.hp
        potion_used = False

        while player_hp > 0 and boss_hp > 0:
            if player_turn:
                # Spieler greift an
                if self.hit_success(self.character.hit_chance()):
                    damage = self.character.attack_damage()
                    boss_hp -= damage
                    ui.notify(f"Du hast {boss.name} für {damage} Schaden getroffen!", color="green")
                else:
                    ui.notify("Du hast verfehlt!", color="red")

                # Option: Trank verwenden
                if not potion_used and player_hp <= self.character.max_hp * 0.5:
                    self.character.use_potion()
                    potion_used = True
            else:
                # Boss greift an
                if self.hit_success(70):  # Standard-Trefferwahrscheinlichkeit des Bosses
                    raw_damage = boss.attack
                    damage = self.character.reduce_damage(raw_damage)
                    player_hp -= damage
                    ui.notify(f"{boss.name} hat dich für {damage} Schaden getroffen!", color="red")
                else:
                    ui.notify(f"{boss.name} hat verfehlt!", color="blue")

            # Wechsel der Runde
            player_turn = not player_turn

        # Kampfergebnis
        if boss_hp <= 0:
            boss.defeated = True
            self.character.add_gold(boss.reward_gold)
            self.character.add_xp(boss.reward_gold * 2)
            self.character.unlock_achievement(f"Besiegt: {boss.name}")
            ui.notify(f"Du hast {boss.name} besiegt und {boss.reward_gold} Gold erhalten!", color="green")
        else:
            ui.notify("Du wurdest besiegt. Der Boss war zu stark.", color="red")

        # Nach dem Kampf HP zurücksetzen
        self.character.hp = player_hp
        self.update_status()
        self.display_fights()

    def buy_item(self, item_name):
        """
        Führt den Kauf eines Items aus und fügt es dem Inventar des Charakters hinzu.
        """
        if item_name in self.shop.items:
            item_info = self.shop.items[item_name]
            if self.character.gold >= item_info["cost"]:
                # Gold abziehen
                self.character.gold -= item_info["cost"]

                # Item hinzufügen
                item_type = item_info["type"]
                self.character.equipment[item_type] = item_info
                ui.notify(f"'{item_name}' wurde erfolgreich gekauft!", color="green")
                self.update_status()
            else:
                ui.notify(f"Nicht genügend Gold für '{item_name}'.", color="red")
        else:
            ui.notify(f"Item '{item_name}' ist nicht verfügbar.", color="red")


if __name__ == "__main__":
    app = ToDoRPGApp("Abenteurer")
    ui.run(static_files={'/assets': 'assets'})
