def stringify(obj):
    return "!-!-" + str(obj) + "-!-!"

def simplify(some_str):
    return some_str.replace("!", "")[:12]

def white_begone(some_str):
    return some_str.trim().replace(" ", "").replace("\t", "")

def indexify(some_str, index):
    result = stringify(index) + some_str
    result = simplify(result)
    if index > 4:
        result = white_begone(result)
    return result


import unittest

class TestIndexify(unittest.TestCase):

    def test_low_index_leaves_whitespace(self):
        """
        indexify leaves whitespace in low indexes
        """
        # Test this without running stringify(), simplify(), or white_begone()

