class Stuff:

    def __init__(self):
        self._stuff = ['a', 'b', 'c', 'd', 'e']

    def get_upper_stuff(self, index):
        """
        Valid, positive index? Return upper.  Else raise NotImplementedError.
        """
        if (index < len(self._stuff)) and (index >= 0):
            return self._stuff[index].upper()
        raise NotImplementedError

import unittest

class TestStuff(unittest.TestCase):

    def test_before_range(self):
        """Index before range raises NotImplementedError"""
        s = Stuff()
        self.assertRaises(NotImplementedError, s.get_upper_stuff, -1,)

    def test_beginning_range(self):
        """Index at beginning of range returns correctly"""
        s = Stuff()
        self.assertEqual(s.get_upper_stuff(0), 'A')

    def test_middle_range(self):
        """Index in middle of range returns correctly"""
        s = Stuff()
        self.assertEqual(s.get_upper_stuff(2), 'C')

    def test_end_range(self):
        """Index at end of range returns correctly"""
        s = Stuff()
        self.assertEqual(s.get_upper_stuff(4), 'E')

    def test_beyond_range(self):
        """Index beyond range returns NotImplementedError"""
        s = Stuff()
        self.assertRaises(NotImplementedError, s.get_upper_stuff, 5,)
