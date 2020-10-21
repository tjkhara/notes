class WeaponDispenser:

    def __init__(self):
        self.weapons = ["katana", "shuriken", "poison"]

    def dispense(self):
        if self.weapons:
            return self.weapons.pop()
        return None

    def easter_egg(self):
        return "EGGS!"
