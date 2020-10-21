import unittest

from armor.color.blue import Blue

# If you want to treat Blue as one unit...

class TestBlue(unittest.TestCase):

    # lighten
    def test_lighten_a_little(self):
        pass

    def test_lighten_a_lot(self):
        pass

    # darken
    def test_darken_a_bit(self):
        pass

    def test_darken_a_ton(self):
        pass

    # texturize
    def test_texturize_soft(self):
        pass

    def test_texturize_smooth(self):
        pass

    def test_texturize_rough(self):
        pass

    # enspecular
    def test_enspecular_maximum(self):
        pass

    def test_enspecular_minimum(self):
        pass

    # etc.


# If "Blue" is so big, you want to consider each method a "unit"...

class TestBlue_Lighten(unittest.TestCase):

    def test_a_little(self):
        pass

    def test_a_lot(self):
        pass


class TestBlue_Darken(unittest.TestCase):

    def test_a_bit(self):
        pass

    def test_a_ton(self):
        pass


class TestBlue_Texturize(unittest.TestCase):

    def test_smooth(self):
        pass

    def test_rough(self):
        pass

class TestBlue_Enspecular(unittest.TestCase):

    def test_maximum(self):
        pass

    def test_minimum(self):
        pass

# etc.

