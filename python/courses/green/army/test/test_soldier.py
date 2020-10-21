import unittest
from army.soldier import Soldier

class TestSoldier(unittest.TestCase):

    def test_pushups(self):
        """
        Soldiers should be able to do atleast 100 pushups.
        """
        s = Soldier()
        self.assertGreaterEqual(s.pushups(), 100, 
        "Soldier was unable to do 100 pushups")

    def test_honor(self):
        """
        Soldiers should server with honor.
        """
        s = Soldier()
        self.assertTrue(s.honor)