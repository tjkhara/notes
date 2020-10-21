import unittest

from mypkg.mymodule import my_function, MyClass

class TestMyFunction(unittest.TestCase):

    def test_does_not_crash(self):
        """
        My function does not crash when called.
        """
        my_function(5)

    def test_true_and_false(self):
        """
        Using assertTrue and assertFalse to test things
        """
        self.assertTrue(my_function(5) == 10)
        self.assertFalse(my_function(2) == 5)

    def test_special_zero(self):
        """
        my_function(0) is special and returns 100
        """
        x = my_function(0)
        if x != 100:
            self.fail("Zero is special the function should return 100 did not return 100")


class TestMyClass(unittest.TestCase):

    def test_counter_starts(self):
        """
        counter starts at 0
        """
        if True:
            self.skipTest("Not implemented yet -- but skipping from inside.")

    def test_id_assigned(self):
        """
        id gets assigned
        """
        pass

    @unittest.skip("Not implemented yet")
    def test_counter_incremented(self):
        """
        counter gets incremented
        """
        pass

    def test_get_id(self):
        """
        get_id() works
        """
        pass

    @unittest.expectedFailure
    def test_unstable_method(self):
        """
        unstable_method() does whatever it wants
        """

        m = MyClass()
        m.unstable_method()