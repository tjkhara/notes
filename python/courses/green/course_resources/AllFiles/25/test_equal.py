import unittest

text1 = u"First Line\nSecond Line\nThird Line"
text2 = u"First Line\n2nd Line\nThird Line"

set1  = set(['one', 'two', 'three'])
set2  = set(['one', 'seven', 'three'])

list1 = ['apple', 'banana', 'cow']
list2 = ['apple', 'xunana', 'cow']

dict1 = {"Mary" : "Jane", "Peter" : "Parker"}
dict2 = {"Mary" : "Jane", "Spider" : "Man"}

tuple1 = ("Hello", "Dolly")
tuple2 = ("Hello", "My", "Sunshine")

class Cow:

    def __init__(self):
        self.hooves = 8

    def __eq__(self, other):
        return self.hooves == other.hooves

class TestEquality(unittest.TestCase):

    def test_assertEqual(self):
        """
        Checking equality...in style.
        """
        # self.assertEqual(1, 2)           # Fails
        #self.assertNotEqual(1, 2)        # Succeeds
        #self.assertEqual(text1, text2)   # Fails - Note the fancy diff!
        #self.assertEqual(list1, list2)   # Fails - Note the fancy diff!
        #self.assertEqual(set1, set2)     # Fails - Note the fancy diff!
        #self.assertEqual(dict1, dict2)   # Fails - Note the fancy diff!
        #self.assertEqual(tuple1, tuple2) # Fails - Note the fancy diff!
        self.assertEqual(Cow(), Cow(), "Cows have different number of legs!") # Tricky!!!
