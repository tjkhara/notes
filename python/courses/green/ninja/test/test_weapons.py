import unittest
from ninja.weapons import WeaponDispenser

class TestWeaponDispenser(unittest.TestCase):

    def test_creation(self):
        """
        WeaponDispenser can be created.
        """
        wd = WeaponDispenser()

    def test_num_weapons(self):
        """
        WeaponDispenser should start with the correct number of weapons.
        """

        wd = WeaponDispenser()
        self.assertTrue(len(wd.weapons) == 3, 
        "There are not three weapons in the dispenser")

    def test_dispense_weapon(self):
        """
        WeaponDispenser dispenses the next weapon
        """
        wd = WeaponDispenser()
        top_of_stack = wd.weapons[-1]
        if wd.dispense() != top_of_stack:
            self.fail("We got the wrong weapon")

    def test_empty_dispenser(self):
        """
        Empty dispenser dispenses None
        """
        wd = WeaponDispenser()
        for i in range(len(wd.weapons)):
            wd.dispense()
        self.assertFalse(wd.dispense(),
        "Empty dispenser ought to dispense None")

    @unittest.skip("TODO: Need designer input about future stuff")
    def test_future_stuff(self):
        """
        Future stuff
        """
        pass

    @unittest.expectedFailure
    def test_easter_egg(self):
        """
        Easter egg... it might work
        """
        wd = WeaponDispenser()
        wd.easter_egg()
