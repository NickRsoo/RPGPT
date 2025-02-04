from nicegui import ui

class Quest:
    def __init__(self, description: str, xp_reward: int, gold_reward: int, difficulty: str, due_date: str):
        self.description = description
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.difficulty = difficulty  # Schwierigkeitsgrad
        self.due_date = due_date  # Abschlussdatum
        self.completed = False

    def complete(self, character) -> bool:
        if not self.completed:
            character.add_xp(self.xp_reward)
            character.add_gold(self.gold_reward)
            self.completed = True
            ui.notify(f"Quest '{self.description}' abgeschlossen!", color="green")
            return True
        else:
            ui.notify(f"Quest '{self.description}' wurde bereits abgeschlossen.", color="red")
            return False
