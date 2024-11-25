from nicegui import ui

class Shop:
    def __init__(self):
        """
        Repräsentiert einen Shop mit einer Liste verfügbarer Items.
        """
        self.items = {
            "Schwert": {
                "cost": 100,
                "description": "Ein starkes Schwert.",
                "icon": "C:/Github/RPGPT/app/assets/shop_Icons/broadsword.png"
            },
            "Schild": {
                "cost": 150,
                "description": "Ein zuverlässiges Schild.",
                "icon": "C:/Github/RPGPT/app/assets/shop_icons/templar-shield.png"
            },
            "Heiltrank": {
                "cost": 50,
                "description": "Stellt Gesundheit wieder her.",
                "icon": "C:/Github/RPGPT/app/assets/shop_icons/heart-bottle.png"
            }
        }

    def buy(self, character, item_name: str) -> bool:
        if item_name not in self.items:
            ui.notify("Item nicht verfügbar.", color="red")
            return False

        item_cost = self.items[item_name]["cost"]
        if character.gold >= item_cost:
            character.gold -= item_cost
            return True
        else:
            ui.notify(f"Nicht genügend Gold für '{item_name}'.", color="red")
            return False

