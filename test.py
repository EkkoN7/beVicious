# Player: name, health endurance, level, exp
# Weapon:user, target,  type,  damage,  curse)

from classes import Mage, Warrior
from weapons import Staff

ekko = Mage("Ekko", 100, 100, 1, 0)
orc = Warrior("Orc", 100, 100, 1, 0)

ice_staff = Staff(ekko, orc, "Ice", 40, 20 )

print(ice_staff.ice)


