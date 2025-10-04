import random

player = random.randint(0, 6)
enemy = random.randint(0,6)
game_over = False
while game_over == False:
    lvl = 1
    user_name = input("Welcome to beVicious.\nWhats your name: ").strip()
    choose_class = input(f"Which class do you choose:\n1: Warrior\n2: Mage\n3: Archer\nInfo: Type 1, 2 or 3\n{user_name}: ").strip()
    if choose_class == "1":
        print(f"From the dust of the arena rises Level {lvl} Warrior {user_name}. May your dead be swift and painless.")
    if choose_class == "2":
        print(f"From the dust of the arena rises Level {lvl} Mage {user_name}. May your dead be swift and painless.")
    if choose_class == "3":
        print(f"From the dust of the arena rises Level {lvl} Archer {user_name}. May your dead be swift and painless.")

