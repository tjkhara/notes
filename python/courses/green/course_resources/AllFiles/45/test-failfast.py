import unittest

class TestFailFast(unittest.TestCase):

    def test_error(self):
        raise Exception

    def test_fail(self):
        self.fail("I fail")

    def test_zpass(self):
        pass

