from nicegui import ui

class Character:
    def __init__(self,name: str):
        self.name = name
        # self.ds = race  # Speichert die gewählte Rasse
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.hp = 100
        self.max_hp = 100



        # Ausrüstung
        self.equipment = {
            "sword": {"name": "Basic Sword", "damage": 10},
            "shield": {"name": "Basic Shield", "block": 2},
            "armor": {"name": "Basic Armor", "hit_chance_bonus": 5},
            "potion": {"name": "Health Potion", "heal": 50, "used": False},
        }

        # Errungenschaften
        self.achievements = []

    def add_xp(self, xp: int):
        self.xp += xp
        if self.xp >= self.level * 100:
            self.level += 1
            self.xp = 0
            self.hp = self.max_hp  # Volle Heilung bei Levelaufstieg
            ui.notify(f"Levelaufstieg! Du bist jetzt Level {self.level}.", color="green")

    def add_gold(self, gold: int):
        self.gold += gold

    def attack_damage(self):
        """
        Berechnet den Angriffsschaden basierend auf dem ausgerüsteten Schwert.
        """
        return self.equipment["sword"]["damage"]

    def reduce_damage(self, damage: int):
        """
        Reduziert eingehenden Schaden basierend auf dem ausgerüsteten Schild.
        """
        block = self.equipment["shield"]["block"]
        return max(damage - block, 0)

    def hit_chance(self):
        """
        Berechnet die Trefferwahrscheinlichkeit basierend auf der Rüstung.
        """
        return 75 + self.equipment["armor"]["hit_chance_bonus"]

    def use_potion(self):
        """
        Verwendet den Heiltrank, um HP wiederherzustellen.
        """
        if not self.equipment["potion"]["used"]:
            self.hp = min(self.hp + self.equipment["potion"]["heal"], self.max_hp)
            self.equipment["potion"]["used"] = True
            ui.notify("Du hast den Heiltrank verwendet und HP regeneriert.", color="blue")
        else:
            ui.notify("Du hast den Heiltrank bereits in diesem Kampf verwendet.", color="red")

    def unlock_achievement(self, achievement: str):
        """
        Schaltet eine Errungenschaft frei, falls sie nicht bereits vorhanden ist.
        """
        if achievement not in self.achievements:
            self.achievements.append(achievement)
            ui.notify(f"Errungenschaft freigeschaltet: {achievement}", color="green")
