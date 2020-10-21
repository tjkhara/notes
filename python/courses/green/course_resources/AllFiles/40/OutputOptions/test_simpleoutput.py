import unittest

class TestSimpleOutput(unittest.TestCase):

    def test_method_name(self):
        """
        With verbosity=3 (-vvv), docstrings are output!
        """
        pass

    def test_positive(self):
        """
        Phrase your docstrings positively.  Like this next one:
        """
        pass

    def test_stuff(self):
        """
        The stuff does the right thing.
        """
        pass

    def test_stuff_discussion(self):
        """
        When it fails, think: "stuff doing the right thing...is failing!"
        """
        pass

    def test_super_long(self):
        """

        Beginning whitespace is stripped.
        The entire first paragraph is reflowed.
        Paragraphs are bounded by a blank line.

        This is part of the second paragraph, because
        there is a blank line separating it.

        The third paragraph is right out.
        """
        pass
