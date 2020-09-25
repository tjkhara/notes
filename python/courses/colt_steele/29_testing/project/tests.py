from card import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("A", "Hearts")

	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		"""repr should return a string of the form 'Value of Suit'"""
		self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""Deck should have a cards attribute which is a list and length of the list should be 52"""
		self.assertEqual(isinstance(self.deck.cards, list), True)
		self.assertEqual(len(self.deck.cards), 52)

	def test_repr(self):
		"""repr should return a string of the form 'Deck of 13 cards'"""
		self.assertEqual(repr(self.deck), f"Deck of {self.deck.count()} cards")

	def test_count(self):
		"""count should return a count of the number of cards"""
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	# Deck  should have an instance method called _deal  which accepts a number and removes at most that 
	# many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). 
	# If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
	def test_deal_sufficient_cards(self):
		"""dealing sufficient cards"""
		cards = self.deck._deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)

	def test_deal_insufficient_cards(self):
		"""_deal should deal only the number of cards left"""
		cards = self.deck._deal(100)
		self.assertEqual(len(cards),52)
		self.assertEqual(self.deck.count(), 0)

	def test_deal_no_cards(self):
		"""test deal when no cards are left - should throw value error"""
		self.deck._deal(self.deck.count())
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_deal_card(self):
		"""deal_card should deal a single card from the deck"""
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(self.deck.count(), 51)

	def test_deal_hand(self):
		cards = self.deck.deal_hand(20)
		self.assertEqual(len(cards), 20)
		self.assertEqual(self.deck.count(), 32)

	# def test_shuffle_full_deck(self):
	# 	cards = self.deck.cards[:]
	# 	self.deck.shuffle()
	# 	self.assertNotEqual(cards, self.deck.cards)
	# 	self.assertEqual(self.deck.count(), 52)

if __name__ == "__main__":
    unittest.main()

# error reference
# def test_eat_healthy_boolean(self):
#     	"""is_healthy must be a bool"""
#     	with self.assertRaises(ValueError):
#     		eat("pizza", is_healthy="who cares?")