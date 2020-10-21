class Animal(object):
    pass

class Puppy(Animal):
    pass

class Rock(object):
    pass

import unittest

class TestAssertIsInstance(unittest.TestCase):

    def test_assert_is_instance(self):
        """
        assertIsInstance fails if arg1 is not an instance of arg2
        """
        # 1) 2nd argument can be a user-defined class
        puppy = Puppy()
        self.assertIsInstance(puppy, Puppy)
        self.assertIsInstance(puppy, Animal)
        #self.assertIs(type(puppy), Animal)
        #self.assertIsInstance(puppy, Rock, "Puppies aren't rocks!?!?")

        # 2) 2nd argument can also be a built-in type
        self.assertIsInstance("a string", str)
        self.assertIsInstance([1, 2, 3], list)

        # 3) 2nd argument can be a tuple of user-defined classes and/or types
        self.assertIsInstance(puppy, (Animal, Rock, str))

    def test_assert_not_is_instance(self):
        """
        assertNotIsInstance is the awkwardly-named opposite
        """
        puppy = Puppy()
        self.assertNotIsInstance(puppy, Rock)
