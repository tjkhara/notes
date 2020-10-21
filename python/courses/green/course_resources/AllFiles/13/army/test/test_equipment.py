import unittest

from army.equipment import Boots, Rifle

class TestBoots(unittest.TestCase):

    def test_color(self):
        """
        Army Boots should be black.
        """
        b = Boots()
        self.assertEqual(b.color, "black")

class TestRifle(unittest.TestCase):

    def test_clean(self):
        """
        Army Rifles should start clean.
        """
        r = Rifle()
        self.assertTrue(r.clean)

    def test_loaded(self):
        """
        Army Rifles should start loaded.
        """
        r = Rifle()
        self.assertTrue(r.loaded)
