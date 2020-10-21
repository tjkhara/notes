class Sprocket:

    def __init__(self, rotation=0, rotation_amount=30):
        self._rotation = (rotation % 360)
        self._rotation_amount = rotation_amount

    def turn(self):
        self._rotation = (self._rotation + self._rotation_amount) % 360

    def rotation(self):
        return self._rotation


import unittest

class TestSprocket(unittest.TestCase):

    def test_sprocket_rotation_boundaries(self):
        """
        No matter what rotation & rotation_amount start at, or how many turns
        are done, the sprocket rotation stays within bounds 0 to 359.
        """
        # rotation is bounded, so test the bounds
        for rotation in [-1, 0, 179, 180, 181, 359, 360]:
            # rotation_amount is unbounded, so pick some interesting values
            for rotation_amount in [-545, -360, -1, 1, 180, 359, 360, 361, 434]:
                sprocket = Sprocket(rotation, rotation_amount)
                # Turn it enough times that it ought to cross the bounds
                for turns in range((360 / abs(rotation_amount)) + 2):
                    self.assertGreaterEqual(sprocket.rotation(), 0)
                    self.assertLessEqual(sprocket.rotation(), 359)
                    sprocket.turn()

# 1. Design Tool
# 2. Readable
# 3. Test One Outcome
# 4. Test Boundaries
# 5. Test Results
# 6. Isolate the Unit
# 7. Identify the Reason
