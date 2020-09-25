import unittest
from activities import eat_food as eat, nap

class ActivityTests(unittest.TestCase):
	def test_eat(self):
		# This is testing eat when we pass in is_healthy=True
		self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli because my body is a temple")
		# This is testing eat when we pass in is_healthy=False
		self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza because YOLO")

if __name__ == "__main__":
	unittest.main() # this line runs the tests