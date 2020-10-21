from mock import patch
import unittest

from spaceship import Laser

class FakeLaser(object):
    sound = "a string"
    def fire(self):
        pass

class TestSpec(unittest.TestCase):

    @patch('spaceship.Laser', autospec=True)
    def test_autospec_true(self, mock_laser):
        mock_laser.fire()
        with self.assertRaises(AttributeError):
            mock_laser.eat_yummy_pie()
        # No sound attribute, though :-(  This would crash:
        # mock_laser.sound

    @patch('spaceship.Laser', autospec=FakeLaser)
    def test_autospec_other_obj(self, mock_laser):
        mock_laser.sound # now this won't crash
