from nicegui import ui
from components.character import Character
from components.shop import Shop
from components.Bosses import Boss
from components.quest import Quest
from ui.database import init_db, save_quest, save_character
init_db()
class ToDoRPGApp:
    def __init__(self, character_name):
        print(f"Spiel wird gestartet mit Name: {character_name},")  # Debugging
        self.character_name = character_name  # Speichert den Namen
        save_character(self.character_name)
        self.character = Character(character_name,)  
        self.shop = Shop()
        self.bosses = self.create_bosses()
        self.quests = []
        self.completed_quests = []

        self.setup_ui()  # UI aufbauen


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
        # Hauptcontainer für die gesamte Seite
        with ui.row().classes('h-screen w-screen flex overflow-hidden'):
            # Linkes Menü (fixiert auf 20%)
            with ui.column().classes('bg-gray-800 text-white w-1/5 h-full p-4'):
                # Charakterbereich (im linken Menü)
                with ui.row().classes('items-center mb-6'):
                    # ui.image(self.avatar["image"]).style("width: 50px; height: 50px; border-radius: 50%;")  # Avatar anzeigen
                    with ui.column().classes('ml-4'):
                        ui.label(f"{self.character_name}") .classes("text-xl font-bold")  # Zeigt Name + Rasse
                        ui.label(f"Gold: {self.character.gold}").classes("text-sm text-yellow-400")


                # Navigationsbuttons
                self.create_nav_button("Taverne", icon="local_bar", section="tavern")
                self.create_nav_button("Fights", icon="swords", section="fights")
                self.create_nav_button("Händler", icon="shopping_cart", section="shop")
                self.create_nav_button("Quarter", icon="house", section="character")
                self.create_nav_button("Achievements", icon="emoji_events", section="achievements")
       
            # Hauptinhalt (80% rechts vom Menü)
            with ui.column().classes('flex-1 h-full p-6 bg-[url("C:/Github/RPGPT/app/assets/background/background.jpg")] bg-cover bg-center overflow-y-auto'):
                # Statusbereich oben
                with ui.row().classes('justify-between items-center bg-white p-4 rounded shadow mb-4'):
                    self.status = ui.label(self.get_status()).classes("text-lg")
                    ui.button("Status aktualisieren", on_click=self.update_status).classes("bg-blue-500 text-white rounded p-2")

                # Dynamischer Hauptinhalt
                self.main_content = ui.column().classes('w-full')
                self.display_tavern()  # Standardanzeige: Taverne

            
 


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
        self.main_content.clear() 
        with self.main_content:
            ui.label("Taverne").classes("text-xl font-bold mb-4")
    
            # Aktive Quests
            ui.label("Aktive Quests").classes("text-lg font-bold mt-2")
            with ui.column().classes('gap-2'):
                for quest in self.quests:
                    with ui.row().classes('items-center gap-4'):
                        ui.label(f"{quest.description} - {quest.xp_reward} XP, {quest.gold_reward} Gold")
                        ui.label(f"Schwierigkeit: {quest.difficulty}, Abschlussdatum: {quest.due_date}")
                        ui.button("Abschließen", on_click=lambda q=quest: self.complete_quest(q))

            # Abgeschlossene Quests
            ui.label("Fertige Quests").classes("text-lg font-bold mt-4")
            with ui.column().classes('gap-2'):
                for quest in self.completed_quests:
                    ui.label(f"{quest.description} - {quest.difficulty}, abgeschlossen am: {quest.due_date}").classes("text-base text-green-600")

            # Neue Quest hinzufügen
            ui.label("Neue Quest hinzufügen").classes("text-lg font-bold mt-4")
            with ui.row().classes('gap-2 mt-2'):
                description_input = ui.input("Beschreibung").classes("w-1/2")
                xp_input = ui.number("XP-Belohnung", value=10, min=1).classes("w-1/6")
                gold_input = ui.number("Gold-Belohnung", value=10, min=1).classes("w-1/6")
                
                # Dropdown für Schwierigkeit
                difficulty_input = ui.select(["Leicht", "Mittel", "Schwer"], value="Mittel").classes("w-1/6")

                # Datumsauswahl für Abschlussdatum
                due_date_input = ui.input("Abschlussdatum (YYYY-MM-DD)").classes("w-1/6")

            ui.button("Hinzufügen", on_click=lambda: self.add_quest(
                    description_input.value,
                    xp_input.value,
                    gold_input.value,
                    difficulty_input.value,
                    due_date_input.value
                ))

    def add_quest(self, description, xp_reward, gold_reward, difficulty, due_date):
        if not description.strip():
            ui.notify("Beschreibung darf nicht leer sein.", color="red")
            return
        if xp_reward <= 0 or gold_reward <= 0:
            ui.notify("Belohnungen müssen größer als 0 sein.", color="red")
            return
        if not due_date:
            ui.notify("Bitte ein Abschlussdatum angeben!", color="red")
            return

        quest = Quest(description, xp_reward, gold_reward, difficulty, due_date)
        self.quests.append(quest)
        # save_quest(description,xp_reward,gold_reward,difficulty,due_date,self.character_name)
        ui.notify(f"Quest '{description}' hinzugefügt!", color="green")
        self.display_tavern()

    def complete_quest(self, quest):
        if quest.complete(self.character):
            self.quests.remove(quest)
            self.completed_quests.append(quest)
            ui.notify(f"Quest '{quest.description}' abgeschlossen!", color="green")
            self.display_tavern()


    def display_fights(self):
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

    def start_fight(self, boss):
            player_turn = True
            boss_hp = boss.hp
            player_hp = self.character.hp
            potion_used = False

            while player_hp > 0 and boss_hp > 0:
                ui.notify(f"Deine HP: {player_hp} | {boss.name} HP: {boss_hp}", color="blue")
                if player_turn:
                    if self.hit_success(self.character.hit_chance()):
                        damage = self.character.attack_damage()
                        boss_hp -= damage
                        ui.notify(f"Du hast {boss.name} für {damage} Schaden getroffen!", color="green")
                    else:
                        ui.notify("Du hast verfehlt!", color="red")
                    if not potion_used and player_hp <= self.character.max_hp * 0.5:
                        self.character.use_potion()
                        potion_used = True
                else:
                    if self.hit_success(70):
                        raw_damage = boss.attack
                        damage = self.character.reduce_damage(raw_damage)
                        player_hp -= damage
                        ui.notify(f"{boss.name} hat dich für {damage} Schaden getroffen!", color="red")
                    else:
                        ui.notify(f"{boss.name} hat verfehlt!", color="blue")
                player_turn = not player_turn

            if boss_hp <= 0:
                boss.defeated = True
                self.character.add_gold(boss.reward_gold)
                self.character.add_xp(boss.reward_gold * 2)
                ui.notify(f"Du hast {boss.name} besiegt und {boss.reward_gold} Gold erhalten!", color="green")
            else:
                ui.notify("Du wurdest besiegt. Der Boss war zu stark.", color="red")

            self.character.hp = player_hp
            self.update_status()
            self.display_fights()

    def display_shop(self):
            self.main_content.clear()
            with self.main_content:
                ui.label("Händler").classes("text-xl font-bold mb-4")
                for item_name, item_info in self.shop.items.items():
                    with ui.row().classes('items-center gap-4'):
                        ui.image(item_info["image"]).style("width: 50px; height: 50px;")
                        ui.label(f"{item_name}: {item_info['cost']} Gold")
                        ui.button(f"Kaufen", on_click=lambda name=item_name: self.buy_item(name))

    def buy_item(self, item_name):
            if item_name in self.shop.items:
                item_info = self.shop.items[item_name]
                if self.character.gold >= item_info["cost"]:
                    self.character.gold -= item_info["cost"]
                    item_type = item_info["type"]
                    self.character.equipment[item_type] = item_info
                    self.shop.items.pop(item_name)
                    ui.notify(f"'{item_name}' wurde erfolgreich gekauft!", color="green")
                    self.display_shop()
                else:
                    ui.notify(f"Nicht genügend Gold für '{item_name}'.", color="red")
            else:
                ui.notify(f"Item '{item_name}' ist nicht verfügbar.", color="red")

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
            """
            Aktualisiert den Status-Label mit aktuellen Werten.
            """
            self.status.set_text(self.get_status())

    def get_status(self):
            return f"Level: {self.character.level}, Gold: {self.character.gold}"

    def hit_success(self, chance: int) -> bool:
            from random import randint
            return randint(1, 100) <= chance
    
    
if  __name__ == "__main__":
    app = ToDoRPGApp("Abenteurer")
    ui.run(static_files={'/assets': 'assets'})
