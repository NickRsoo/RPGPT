class Boss:
    def __init__(self, name: str, level_required: int, hp: int, attack: int, reward_gold: int):
        self.name = name
        self.level_required = level_required
        self.hp = hp
        self.attack = attack
        self.reward_gold = reward_gold
        self.defeated = False

    def take_damage(self, damage: int):
        """
        Verringert die HP des Bosses um den angegebenen Schaden.
        """
        self.hp -= damage
        return self.hp <= 0
