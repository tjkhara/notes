class MyMovableObject():

    def __init__(self, start_x, start_y):
        self._x, self._y = start_x, start_y

    def moveUp(self, amount):
        self.move(0, amount)

    def move(self, x, y):
        self._x += x
        self._y += y

    def currCoords():
        return (self._x, self._y)

class TestMyClass(unittest.TestCase):

    def test_move_up(self):
        myobject = MyMovableObject(start_x=1, start_y=5)
        myobject.moveUp(1)
        self.assertEqual(myobject.currCoords(), (1, 6))

