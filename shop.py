# shop.py
from nicegui import ui

class Shop:
    def __init__(self):
        self.items = {
            "Elixier des Wissens": {"cost": 50, "effect": lambda char: char.add_xp(50)},
            "Goldene Feder": {"cost": 100, "effect": lambda char: char.add_xp(100)},
            "Schatzkiste": {"cost": 200, "effect": lambda char: char.add_gold(200)}
        }

    def buy(self, character, item_name):
        item = self.items.get(item_name)
        if item and character.gold >= item["cost"]:
            character.gold -= item["cost"]
            item["effect"](character)
            ui.notify(f"{character.name} hat {item_name} gekauft!")
        else:
            ui.notify("Nicht genug Gold oder Item existiert nicht.")
