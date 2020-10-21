import unittest

list1 = ['a', 'b', 'c']
list2 = ['a', 'b', 'c']
list3 = ['c', 'b', 'a']
list4 = ['a', 'b', 'c', 'c']
list5 = ['x']

class TestItemsEqual_or_CountEqual(unittest.TestCase):

    def test_items_equal(self):
        """
        (Python 2) assertItemsEqual == (Python 3) assertCountEqual
        """
        # In Python 3 this would be:
        # self.assertCountEqual(list1, list2)
        self.assertItemsEqual(list1, list2)

        # Passes, because both lists have the same number of the same items.
        # Equivalent to: assertEqual(sorted(list1), sorted(list2))
        self.assertItemsEqual(list1, list3)

        # Fails, because list4 has a different number of 3's
        #self.assertItemsEqual(list1, list4)

        # Also fails, for obvious reasons
        #self.assertItemsEqual(list1, list5, "Happy Days Are Here Again!")

