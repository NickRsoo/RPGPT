from nicegui import ui

class Shop:
    def __init__(self):
        """
        Repräsentiert einen Shop mit einer Liste verfügbarer Items.
        """
        self.items = {
            "Schwert": {"cost": 100, "description": "Ein starkes Schwert."},
            "Schild": {"cost": 150, "description": "Ein zuverlässiges Schild."},
            "Heiltrank": {"cost": 50, "description": "Stellt Gesundheit wieder her."}
        }

    def buy(self, character, item_name: str) -> bool:
        """
        Ermöglicht es dem Charakter, ein Item zu kaufen, falls genügend Gold vorhanden ist.

        Args:
            character: Der Charakter, der das Item kaufen möchte.
            item_name: Der Name des zu kaufenden Items.

        Returns:
            bool: True, wenn der Kauf erfolgreich war, False bei unzureichendem Gold.
        """
        if item_name not in self.items:
            ui.notify("Item nicht verfügbar.", color="red")
            return False

        item_cost = self.items[item_name]["cost"]
        if character.gold >= item_cost:
            character.gold -= item_cost
            ui.notify(f"'{item_name}' erfolgreich gekauft!", color="green")
            return True
        else:
            ui.notify(f"Nicht genügend Gold für '{item_name}'.", color="red")
            return False
