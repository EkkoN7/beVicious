class Mage:
    def __init__(self, name: str, health: int, mana: int):
        self.name = name
        self.health = health
        self.mana = mana

    def ice_ray(self, target, damage: int, mana_cost: int):
        if self.mana > mana_cost:
            self.mana -= mana_cost
            if target.health > damage:
                target.health -= damage
                print(f"{target.name} has been hit for {damage} damage point")
            else:
                target.health -= damage
                print(f"{target.name} has died :(")

class Warrior:
    def __init__(self, name: str, health: int, endurance: int):
        self.name = name
        self.health = health
        self.endurance = endurance

    def slash(self, target, damage: int, endurance_cost: int):
        if self.endurance > endurance_cost:
            self.mana -= endurance_cost
            if target.health > damage:
                target.health -= damage
                print(f"{target.name} has been hit for {damage} damage point")
            else:
                target.health -= damage
                print(f"{target.name} has died :(")

class Archer:
    def __init__(self, name: str, health: int, endurance: int):
        self.name = name
        self.health = health
        self.endurance = endurance

    def shoot(self, target, damage: int, endurance_cost: int):
        if self.endurance > endurance_cost:
            self.mana -= endurance_cost
            if target.health > damage:
                target.health -= damage
                print(f"{target.name} has been hit for {damage} damage point")
            else:
                target.health -= damage
                print(f"{target.name} has died :(")