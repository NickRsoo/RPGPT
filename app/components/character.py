from nicegui import ui

class Character:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.achievements = []
        self.items = {}  # Dictionary für gekaufte Items

    def add_item(self, item_name: str, item_info: dict):
        """
        Fügt ein gekauftes Item zur Charakter-Item-Liste hinzu.
        """
        if item_name not in self.items:
            self.items[item_name] = item_info



    def add_xp(self, xp: int):
        """
        Fügt XP hinzu und erhöht den Level, falls genügend XP gesammelt wurden.
        """
        self.xp += xp
        while self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1

    def add_gold(self, gold: int):
        """
        Fügt dem Charakter Gold hinzu.
        """
        self.gold += gold

    def unlock_achievement(self, achievement: str):
        """
        Fügt eine Errungenschaft hinzu, wenn sie noch nicht freigeschaltet wurde.
        """
        if achievement not in self.achievements:
            self.achievements.append(achievement)
