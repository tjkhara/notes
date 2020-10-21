from mock import patch         # Python 3: from unittest.mock import patch
from StringIO import StringIO  # Python 3: from io import StringIO
import unittest

from spaceship import Xwing

class TestXwing(unittest.TestCase):

    def test_fires_by_call(self):
        """
        When an Xwing fires, it fires four weapons.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('spaceship.Laser') as mock_laser:
                mock_laser.return_value.fire.return_value = "Bang!"
                xwing = Xwing()
                xwing.fire()
                self.assertEqual(mock_laser.return_value.fire.call_count, 4)

    def test_fires_by_value(self):
        """
        When an Xwing fires, the weapon's fire() value gets printed 4 times.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('spaceship.Laser') as mock_laser:
                mock_laser.return_value.fire.return_value = "Bang!"
                xwing = Xwing()
                xwing.fire()
                self.assertEqual(mock_stdout.getvalue().count("Bang!"), 4)

