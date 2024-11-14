# quest.py
from nicegui import ui

class Quest:
    def __init__(self, description, xp_reward, gold_reward):
        self.description = description
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.completed = False

    def complete(self, character):
        if not self.completed:
            character.add_xp(self.xp_reward)
            character.add_gold(self.gold_reward)
            self.completed = True
            ui.notify("Quest abgeschlossen!")
            return True
        else:
            ui.notify("Quest bereits abgeschlossen!")
            return False
