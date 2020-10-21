class Goblin:

    def __init__(self):
        self.health = 100

    def damage(self):
        self.health -= 5
        if self.health <= 0:
            return "Death...death.....death.......I have died!"
        return "Ouch!"

import unittest

def setUpModule():
    global monster_list
    monster_list = []

def tearDownModule():
    global monster_list
    del(monster_list)

class TestGoblin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        TestGoblin.counter = 0

    @classmethod
    def tearDownClass(self):
        del(TestGoblin.counter)

    def setUp(self):
        self.goblin = Goblin()
        self.goblin.health = 1
        TestGoblin.counter += 1
        print("counter is {}".format(TestGoblin.counter))

    def tearDown(self):
        del(self.goblin)

    def test_dying(self):
        self.assertIn("death", self.goblin.damage())

    def test_dying_again(self):
        self.goblin.damage() # first death
        self.assertIn("death", self.goblin.damage()) # second death

class TestMonsters(unittest.TestCase):

    def test_monsters_start_alive(self):
        global monster_list
        for Monster in monster_list:
            m = Monster()
            self.assertGreater(m.health, 0)
