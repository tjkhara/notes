from mock import patch
import unittest

from spaceship import TurboLaser, Frigate

class LightSaber(object):
    def __init__(self):
        raise NotImplementedError()

class TestStuff(unittest.TestCase):

    @patch('test_location.LightSaber')
    def test_local(self, mock_lightsaber_class):
        this_wont_crash = LightSaber()

    @patch('spaceship.TurboLaser')
    def test_other_file(self, mock_turbolaser):
        # This is a "real" frigate with mocked TurboLasers.
        frigate = Frigate()
