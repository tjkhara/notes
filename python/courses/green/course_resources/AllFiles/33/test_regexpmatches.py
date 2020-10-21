import re
import unittest

text = "Pumpkins fall from the sky!"

class TestRegexpMatches(unittest.TestCase):

    def test_regexp_matches(self):
        """
        Strings match the regular expression.
        """
        self.assertRegexpMatches(text, "^Pumpkins.*")
        self.assertRegexpMatches(text, ".*from the.*")

        pattern = re.compile(".*sky!")
        self.assertRegexpMatches(text, pattern)

        #self.assertRegexpMatches(text, "xyz", "Message Prefix")

    def test_not_regexp_matches(self):
        """
        Strings don't match the regular expression.
        """
        self.assertNotRegexpMatches(text, ".*MONSTERS.*")
