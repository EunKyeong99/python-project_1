class character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return(f"{self.name} - HP : {self.hp}, 공격력 : {self.attack}, 방어력 : {self.defense}")
class Hero(character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.role = role
        self.exp = 0

    def gain_exp(self, amount):
        self.exp += amount

    def special_attack(self):
        if self.role == "전사":
            return self.attack + 4
        elif self.role == "마법사":
            return self.attack + 3
        else:
            return self.attack + 5

    def __str__(self):
        return(f"{self.name} - HP : {self.hp}, 공격력 : {self.attack}, 방어력 : {self.defense}, 경험치 : {self.exp}")


class Monster(character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
