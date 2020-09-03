import random

class Card:

	allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self, suit, value):
		if suit not in Card.allowed_suits:
			raise ValueError("You have entered an invalid suit")
		if value not in Card.allowed_values:
			raise ValueError("You have entered an invalid value")
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:

	def __init__(self):
		Hearts = [Card("Hearts", "A"), Card("Hearts", "2"), Card("Hearts", "3"), Card("Hearts", "4"), Card("Hearts", "5"), Card("Hearts", "6"), Card("Hearts", "7"), Card("Hearts", "8"), Card("Hearts", "9"), Card("Hearts", "10"), Card("Hearts", "J"), Card("Hearts", "Q"), Card("Hearts", "K")]
		Diamonds = [Card("Diamonds", "A"), Card("Diamonds", "2"), Card("Diamonds", "3"), Card("Diamonds", "4"), Card("Diamonds", "5"), Card("Diamonds", "6"), Card("Diamonds", "7"), Card("Diamonds", "8"), Card("Diamonds", "9"), Card("Diamonds", "10"), Card("Diamonds", "J"), Card("Diamonds", "Q"), Card("Diamonds", "K")]
		Clubs = [Card("Clubs", "A"), Card("Clubs", "2"), Card("Clubs", "3"), Card("Clubs", "4"), Card("Clubs", "5"), Card("Clubs", "6"), Card("Clubs", "7"), Card("Clubs", "8"), Card("Clubs", "9"), Card("Clubs", "10"), Card("Clubs", "J"), Card("Clubs", "Q"), Card("Clubs", "K")]
		Spades = [Card("Spades", "A"), Card("Spades", "2"), Card("Spades", "3"), Card("Spades", "4"), Card("Spades", "5"), Card("Spades", "6"), Card("Spades", "7"), Card("Spades", "8"), Card("Spades", "9"), Card("Spades", "10"), Card("Spades", "J"), Card("Spades", "Q"), Card("Spades", "K")]
		self.cards = []
		self.cards.extend(Hearts)
		self.cards.extend(Diamonds)
		self.cards.extend(Clubs)
		self.cards.extend(Spades)

		

	# this returns the number of cards remaining in the deck
	def count(self):
		return len(self.cards)


	def print_cards(self):
		for card in self.cards:
			print(card)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	# method accepts a number and removes at most that many cards from the deck
	# it may need to remove fewer if you request more cards than are currently
	# in the deck
	def _deal(self, number):
		# how many cards are in the deck
		cards_in_deck = self.count()
		# is the number requested more than this?
		if cards_in_deck == 0:
			raise ValueError("All cards have been dealt.")
		if number > cards_in_deck:
			raise ValueError(f"You can't remove {number} of cards as there are only {cards_in_deck} cards left.")
		# if the number is in the right range we need to remove as many cards from the deck
		# now to deal

		# create a list of cards that are dealt
		dealt_cards = []

		for x in range(number):
			dealt_cards.append(self.cards.pop())

		#return the dealt_cards
		return dealt_cards

	# shuffle
	# only a full deck can be shuffled
	def shuffle(self):
		if self.count() == 52:
			# randomly shuffle the list
			random.shuffle(self.cards)
			return self.cards		
		else:
			raise ValueError("Only a full deck can be shuffled.")

	#deal_card
	# deal a single card and return that card
	def deal_card(self):
		card_list = self._deal(1)
		return card_list[0]

	#deal_hand
	# Accepts a number of cards and deals that number of cards
	# Returns the list of dealt cards
	def deal_hand(self, number):
		dealt_cards = self._deal(number)
		return dealt_cards


deck_1 = Deck()

card_1 = deck_1.deal_card()
print(card_1)
print(deck_1.count())

card_2 = deck_1.deal_card()
print(card_2)
print(deck_1.count())

hand_1 = deck_1.deal_hand(10)
print(hand_1)

print(deck_1)
