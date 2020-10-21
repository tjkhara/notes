import unittest

class TestIsAndIsNot(unittest.TestCase):

    def test_is(self):
        """
        assertIs checks to see if the arguments are the same object
        """
        # This does NOT test equality -- CPython just happens to re-use integer
        # literals since they are immutable.
        #self.assertIs(1, 1)
        #print id(1), id(1)

        # It is easier to see what is going on with mutable objects like lists
        #a = []
        #b = []
        #c = a
        #self.assertIs(a, c)

        dict1 = dict2 = {"weapon": "sword"}
        self.assertIs(dict1, dict2)

    def test_is_not(self):
        """
        assertIsNot checks to see if the arguments are not the same object
        """
        self.assertIsNot([], [])

    def test_is_none(self):
        """
        assertIsNone checks to see if the argument is the None object
        """
        self.assertIsNone(None)

    def test_is_not_none(self):
        """
        assertIsNotNone checks to see if the argument is not the None object
        """
        self.assertIsNotNone("literally any other object")
