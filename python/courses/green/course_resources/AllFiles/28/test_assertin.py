import unittest

my_languages = ["Rust", "Python", "C++", "C", "TCL", "Javascript"]

class TestAssertIn(unittest.TestCase):

    def test_assert_in(self):
        """
        assertIn causes a test to fail if arg1 is not in arg2
        """
        self.assertIn("Python", my_languages)
        #self.assertIn("Haskell", my_languages)
        #self.assertIn("Assembly", my_languages, "Oh no! We forgot assembly!")

    def test_assert_not_in(self):
        """
        assertNotIn causes a test to fail if arg1 IS in arg2
        """
        self.assertNotIn("Java", my_languages)
