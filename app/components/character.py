class Character:
    def __init__(self, name: str):
        """
        Repräsentiert einen Charakter mit Name, Level, XP, Gold und Errungenschaften.
        """
        self.name = name
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.achievements = []

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
