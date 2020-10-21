import sys
import unittest

# Unconditionally skip the entire class -- please don't do this!
@unittest.skip("I am foolish and don't want to ever run this test.")
class TestSkipClass(unittest.TestCase):

    def test_never_run(self): # This will never be run
        pass

class TestSkipMethod(unittest.TestCase):

    # Unconditionally skip this test -- please don't do this!
    @unittest.skip("I just wanted to write it, not run it.")
    def test_skip_method(self):
        pass

    # Conditional skipping -- good way to skip when you are forced to.
    @unittest.skipIf(sys.platform == "darwin", "This stuff can't run on macOS")
    def test_platform_specific_stuff(self):
        pass

    # Just like skipIf, with inverted logic.
    @unittest.skipUnless(sys.platform == "windows", "Can't run this on windows")
    def test_awesome_non_windows_stuff(self):
        pass

    # Another good way to skip when you are forced to.  Especially if your logic
    # doesn't fit neatly into a one-line expression.
    def test_skip_test(self):
        stuff_is_installed = False
        if not stuff_is_installed:
            self.skipTest("We can't run this because stuff isn't installed.")

    # Yet another way to do things.  Someone must have been channeling Perl.
    def test_skiptest_exception(self):
        external_dependency_ready = False
        if not external_dependency_ready:
            raise unittest.SkipTest("The external dependency isn't ready.")
