import unittest

class TestComplexOutput(unittest.TestCase):

    def test_stdout(self):
        """
        This test writes to stdout.
        """
        print("Hello, world!")

    def test_stderr(self):
        """
        This test writes to stderr.
        """
        print("Goodbye, cruel world!")

    @unittest.skip("My skip reasons are my own.")
    def test_skip(self):
        """
        This test will be skipped.
        """
        pass

