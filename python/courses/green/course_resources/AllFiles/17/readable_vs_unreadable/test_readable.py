import unittest

import mylib.subpkg.module.submodule import item

# We're going to re-use these colors for several tests
red   = (1, 0, 0)
green = (0, 1, 0)
blue  = (0, 0, 1)

class TestItemCreatorFunction(unittest.TestCase): # [0]

    def test_red_feather(self): # [1]
        """
        We can create a red feather
        """
        created_item = item(
            collection_id = 1, # arbitrary
            variant = 15,      # feather variant 15 should is the red one
            item = "feather",
            spawn=True)
        self.assertEqual(returned_item.color, red)
