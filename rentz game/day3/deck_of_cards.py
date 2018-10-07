import random



# Create the Card class with value and suit arguments
class Card:

	def __init__(self, value, suit):

		self.value = value
		self.suit = suit

	def show(self):

		if self.value == 11:
			self.value = "Jack"
		elif self.value == 12:
			self.value = "Queen"
		elif self.value == 13:
			self.value = "King"
		elif self.value == 14:
			self.value = "Ace"
		else:
			self.value = self.value

		print ("{} of {}".format(self.value,self.suit))
		



class Deck:

	def __init__(self):

		self.cards = []
		self.make_deck()


	def make_deck(self):

		for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
			for v in range(2,15):
				self.cards.append(Card(v,s))

	def deal_hand(self):

		rand_card = random.randint(0, len(self.cards) - 1)
		card_dealt = self.cards.pop(rand_card)
		return card_dealt


	def show(self):
		for c in self.cards:
			c.show()

class Player:

	def __init__(self):

		self.hand = []

	def draw_cards(self, deck, number_cards):
		for c in range(number_cards):
			card = deck.deal_hand()
			if card:
				self.hand.append(card)
			else:
				return False

	def show_hand(self):
		for c in self.hand:
			c.show()

pachet = Deck()




guy = Player()
guy.draw_cards(pachet, 3)
guy.show_hand()
