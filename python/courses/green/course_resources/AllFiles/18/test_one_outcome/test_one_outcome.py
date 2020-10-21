import unittest

from mylib import Widget

class GoodExample(unittest.TestCase):

    def setUp(self):
        self.w = Widget()

    def test_starting_values(self):
        """
        Widgets start with correct values (unsprocketed with mass of 5)
        """
        self.assertEqual(self.w.state, "unsprocketed")
        self.assertEqual(self.w.mass, 5)

    def test_sprocketed(self):
        """
        When you sprocket a widget, it gains mass
        """
        self.w.sprocket()
        self.assertGreaterEqual(self.w.mass, 10)
        self.assertEqual(self.w.state, "sprocketed")

    def test_sproinged(self):
        """
        If you sprocket the widget too much, it sproings
        """
        for i in range(50):
            self.w.sprocket()
        self.assertEqual(self.w.state, "sproinged")

    def test_splatted(self):
        """
        If you drop a new widget, it splats
        """
        self.w.drop()
        self.assertEqual(self.w.state, "splatted")

    def test_spluts(self):
        """
        Dropping a used widget spluts instead
        """
        self.w.used = True
        self.w.drop()
        self.assertEqual(self.w.state, "splutted")

