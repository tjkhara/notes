import unittest

def noerror(): pass

def noargs():
    raise KeyError("For the beauty of the Earth.")

def lotsofargs(a, b, c="", d=5):
    raise ValueError

class TestAssertRaises(unittest.TestCase):

    def test_assert_raises(self):
        """
        assertRaises checks to see if an expected exception is raised
        """
        self.assertRaises(KeyError, noargs)
        #self.assertRaises(KeyError, noerror)
        self.assertRaises(ValueError, lotsofargs, 1, 2, c="!", d=4)

        # The exception argument can be a tuple of exceptions
        self.assertRaises((KeyError, ValueError), noargs)

    def test_assert_raises_context_manager(self):
        """
        assertRaises can return a context manager so you can catch exceptions
        from inline test code.
        """
        with self.assertRaises(KeyError) as context_manager:
            raise KeyError("Applesauce")
        #print(context_manager.exception.message)


    def test_assert_raises_regexp(self):
        """
        assertRaisesRegexp checks to see if an Exception was raised AND the
        string representation of the exception raised matches an expected
        pattern.
        """
        self.assertRaisesRegexp(KeyError, '.*beauty.*', noargs)
        #self.assertRaisesRegexp(KeyError, '.*ugliness.*', noargs)
