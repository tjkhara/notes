import unittest

class TestAssertAlmostEqual(unittest.TestCase):

    def test_assert_almost_equal(self):
        """
        assertAlmostEqual checks float values
        """
        self.assertAlmostEqual(1.0, 1.00000001)
        #self.assertAlmostEqual(1.0, 1.00000009)
        self.assertAlmostEqual(1.0, 1.0000001, places=6)
        self.assertAlmostEqual(1.0, 1.001, delta=.01)
        #self.assertAlmostEqual(1.0, 1.1, msg="Not close enough.")

    def test_assert_not_almost_equal(self):
        """
        assertNotAlmostEqual is (not assertAlmostEqual)
        """
        self.assertNotAlmostEqual(3.1, 3.3)
