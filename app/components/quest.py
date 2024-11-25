from nicegui import ui

class Quest:
    def __init__(self, description: str, xp_reward: int, gold_reward: int):
        """
        Repräsentiert eine Quest mit einer Beschreibung, XP- und Gold-Belohnung.
        """
        self.description = description
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.completed = False

    def complete(self, character) -> bool:
        """
        Versucht, die Quest abzuschließen. Vergibt Belohnungen an den Charakter, falls sie erfolgreich abgeschlossen wird.

        Args:
            character: Der Charakter, der die Quest abschließt.

        Returns:
            bool: True, wenn die Quest erfolgreich abgeschlossen wurde, False, wenn sie bereits abgeschlossen war.
        """
        if not self.completed:
            character.add_xp(self.xp_reward)
            character.add_gold(self.gold_reward)
            self.completed = True
            ui.notify(f"Quest '{self.description}' abgeschlossen!", color="green")
            return True
        else:
            ui.notify(f"Quest '{self.description}' wurde bereits abgeschlossen.", color="red")
            return False
