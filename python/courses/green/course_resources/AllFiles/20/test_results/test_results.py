class Incrementer:

    def __init__(self):
        self._list = []

    def increment(self):
        self._list.append(None)

    def amount(self):
        return len(self._list)


import unittest

class TestImplementation(unittest.TestCase):

    def test_incrementing_appends_None_to_list(self):
        """
        Test that the incrementer was implemented how we implemented it.
        """
        i = Incrementer()
        self.assertEqual(i._list, [])
        i.increment()
        self.assertEqual(i._list, [None])


class TestResults(unittest.TestCase):

    def test_incrementer_increments(self):
        """
        Test that we get the results from incrementer that we want.
        """
        i = Incrementer()
        starting_amount = i.amount()
        i.increment()
        self.assertEqual(i.amount(), starting_amount + 1)

