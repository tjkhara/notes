from mock import patch         # Python 3: from unittest.mock import patch
from StringIO import StringIO  # Python 3: from io import StringIO
import unittest

from spaceship import Xwing

class TestXwing(unittest.TestCase):

    def setUp(self):
        stdout_patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = stdout_patcher.start()
        self.addCleanup(stdout_patcher.stop)

        laser_patcher = patch('spaceship.Laser')
        self.mock_laser = laser_patcher.start()
        self.addCleanup(laser_patcher.stop)

    def test_fires_by_call(self):
        """
        When an Xwing fires, it fires four weapons.
        """
        self.mock_laser.return_value.fire.return_value = "Bang!"
        xwing = Xwing()
        xwing.fire()
        self.assertEqual(self.mock_laser.return_value.fire.call_count, 4)

    def test_fires_by_value(self):
        """
        When an Xwing fires, the weapon's fire() value gets printed 4 times.
        """
        self.mock_laser.return_value.fire.return_value = "Bang!"
        xwing = Xwing()
        xwing.fire()
        self.assertEqual(self.mock_stdout.getvalue().count("Bang!"), 4)

