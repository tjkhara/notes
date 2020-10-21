class MyMovableObject():

    def move(self, x, y):
        self._x += x
        self._y += y

    def getX():
        return self._x

    def getY():
        return self._y

class MyMovableObjectFactory():

    def initialize(self, start_x, start_y):
        self.start_x = start_x; self.start_y = start_y

    def produceMovableObject(self):
        m = MovableObject()
        m._x, m._y = (self.start_x, self.start_y)
        return m

class TestMyClass(unittest.TestCase):

    def test_move_up(self):
        factory = MyMovableObjectFactory()
        factory.initialize(start_x=1, start_y=5)
        myobject = factory.produceMovableObject()
        myobject.move(x = 0, y = 1)
        self.assertEqual(myobject.getX(), 1)
        self.assertEqual(myobject.getY(), 6)


















    def test_move_up(self):
        myobject = MyMovableObject(start_x=1, start_y=5)
        myobject.moveUp(1)
        self.assertEqual(myobject.currCoords(), (1, 6))

