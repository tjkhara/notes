import unittest

from mypkg.mymodule import my_function

class TestMyFunction(unittest.TestCase):

    def test_does_not_crash(self):
        """
        my_function() does not crash when called
        """
        my_function(5)
