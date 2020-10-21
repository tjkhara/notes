import unittest

class TestGreaterLess(unittest.TestCase):

    def test_greater(self):
        """
        assertGreater example       >
        """
        self.assertGreater(2, 1)
        self.assertGreater(100, 0)
        self.assertGreater(100, 99)
        #self.assertGreater(100, 200)
        #self.assertGreater(100, 200, "I could have sworn 100 > 200")

    def test_greater_equal(self):
        """
        assertGreaterEqual example  >=
        """
        self.assertGreaterEqual(0, 0)
        self.assertGreaterEqual(1, 0)
        self.assertGreaterEqual(100, 0)

    def test_less(self):
        """
        assertLess example          <
        """
        self.assertLess(99, 100)
        self.assertLess(-500, 100)

    def test_less_equal(self):
        """
        assertLessEqual             <=
        """
        self.assertLessEqual(0, 0)
        self.assertLessEqual(0, 100)
