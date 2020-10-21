class Goblin:

    def __init__(self):
        self.health = 100

    def damage(self):
        self.health -= 5
        if self.health <= 0:
            return "Death...death.....death.......I have died!"
        return "Ouch!"

import unittest

class TestGoblin(unittest.TestCase):

    def test_dying(self):
        g = Goblin()
        self.assertIn("death", g.damage())

    def test_dying_again(self):
        g = Goblin()
        g.damage() # first death
        self.assertIn("death", g.damage()) # second death

class TestMonsters:

    def test_monsters_start_alive(self):
        for Monster in [Goblin]:
            m = Monster()
            self.assertGreater(m.health, 0)
