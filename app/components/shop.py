from nicegui import ui

class Shop:
    def __init__(self):
        self.items = {
            "Iron Sword": {
                "type": "sword",
                "cost": 50,
                "damage": 15,
                "image": "C:/Github/RPGPT/app/assets/shop_icons/broadswordsword.png"
            },
            "Steel Shield": {
                "type": "shield",
                "cost": 40,
                "block": 5,
                "image": "C:/Github/RPGPT/app/assets/shop_icons/templar-shield.png"
            },
            "Leather Armor": {
                "type": "armor",
                "cost": 60,
                "hit_chance_bonus": 10,
                "image": "C:/Github/RPGPT/app/assets/shop_icons/leather_armor.png"
            },
            "Health Potion": {
                "type": "potion",
                "cost": 30,
                "heal": 50,
                "used": False,
                "image": "C:/Github/RPGPT/app/assets/shop_icons/heart_bottle.png"
            },
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

