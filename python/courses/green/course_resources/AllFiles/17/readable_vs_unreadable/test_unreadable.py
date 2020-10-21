import unittest

import mylib

class T(unittest.TestCase): # [0]

    def test_01(self): # [1]
        # [2]

        a = 1 # [3]
        b = 0
        c = 0

        # [4] [5] [6]
        self.assertTrue(mylib.subpkg.module.submodule.item(1, 15, "feather", True).color == (a, b, c))


# What have we here?
#
# [0] Underscriptive class name
# [1] Undescriptive method name
# [2] No docstring *at all*
# [3] Unintelligible one-letter variable names
# [4] Apparently the author suddenly ran out of lines and decided to make that
#   last one count...
# [5] Magic numbers!
# [6] To top it all off, equality is being tested with assertTrue (sigh)

