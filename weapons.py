class Staff:
    def __init__(self, user, target, type: str, damage: int, curse: int):
        self.type = type
        self.damage = damage
        self.curse = curse

        def ice(self):
            ice_ray = 0.5 * user.level
            ice_ray_cost = 10 + user.level
            blizzard = 1 * user.level
            blizzard_cost = 20 + user.level
            if self.type == "Ice":
                choice = input("Choose:\n1) Ice Ray\n2) Blizzard")
                if choice == "1":
                    if user.mana > ice_ray_cost:
                        total_damage = self.damage * ice_ray
                        print(f"{self.user} is casting Ice Ray. {target.name} is taking {total_damage}.")
                        if target.heath > self.damage:
                            target.health -= self.damage
                            print(f"In front of {user.name} staff is beaming a cold ray which freezes the enemy. {target.name} has {target.health} life left.")
                        else:
                            target.health -= self.damage
                            print(f"{target.name} is dead.")
                    else:
                        print(f"{user.name} does not have enough Mana.")
                if choice == "2":
                    if user.mana > blizzard_cost:
                        total_damage = self.damage * blizzard
                        print(f"{self.user} is casting Blizzard. {target.name} is taking {total_damage}.")
                        if target.heath > self.damage:
                            target.health -= self.damage
                            print(f"{user.name} is whispering some words. The air gets chilly and bones are cracking or is it just ice... .{target.name} has {target.health} life left.")
                        else:
                            target.health -= self.damage
                            print(f"{target.name} is dead.")
                    else:
                        print(f"{user.name} does not have enough Mana.")


class Sword:
    def __init__(self, user: str, target: str, type: str, damage: int, cost: int, curse: int):
        self.user = user
        self.type = type
        self.damage = damage
        self.cost = cost
        self.curse = curse


class Bow:
    def __init__(self, user: str, target: str, type: str, damage: int, cost: int, curse: int):
        self.user = user
        self.type = type
        self.damage = damage
        self.cost = cost
        self.curse = curse
