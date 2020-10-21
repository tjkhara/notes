import unittest

from mylib import Widget

class BadExample(unittest.TestCase):

    def test_all_the_things(self):
        """
        In this test we will test everything we can possibly think of.
        """
        # Widgets start unsprocketed
        w = Widget()
        self.assertEqual(w.state, "unsprocketed")

        # When you sprocket a widget, it gains mass
        w.sprocket()
        self.assertGreaterEqual(w.mass, 10)
        self.assertEqual(w.state, "sprocketed")

        # If you sprocket the widget too much, it sproings
        for i in range(50):
            w.sprocket()
        self.assertEqual(w.state, "sproinged")

        # If you drop a new widget, it splats
        w = Widget()
        w.drop()
        self.assertEqual(w.state, "splatted")

        # But a used widget spluts instead
        w = Widget(used=True)
        w.drop()
        self.assertEqual(w.state, "splutted")

