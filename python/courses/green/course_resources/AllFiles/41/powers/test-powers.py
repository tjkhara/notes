import unittest
from mock import patch

from powers import getPowers


class TestGetPowers_FunctionalTests(unittest.TestCase):

    def test_getPowers(self):
        self.assertEqual(getPowers(), set(['flamestrike', 'blizzard']))


class TestGetPowers_UnitTests(unittest.TestCase):

    @patch('powers.cursor')
    def test_getPowers(self, mock_cursor):
        mock_cursor.execute.return_value = [('a', 1, 2), ('b', 3, 4)]
        self.assertEqual(getPowers(), set(['a', 'b']))
