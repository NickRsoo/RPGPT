# character.py
from nicegui import ui

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.achievements = []

    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.xp -= self.level * 100
        self.level += 1
        ui.notify(f"{self.name} ist auf Level {self.level} aufgestiegen!")

    def add_gold(self, amount):
        self.gold += amount
        ui.notify(f"{self.name} hat {amount} Gold erhalten!")

    def add_achievement(self, achievement):
        self.achievements.append(achievement)
        ui.notify(f"Achievement erhalten: {achievement}!")

