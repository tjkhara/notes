import unittest
from army.equipment import Equipment

class TestEquipment(unittest.TestCase):

    def test_number(self):
        """
        Equipment number should be 10.
        """
        e = Equipment()
        self.assertEqual(e.number, 10,
        "Number is not 10")