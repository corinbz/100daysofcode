import random



player1 = []
player2 = []
player3 = []
player4 = []
# Create the deck of cards with suits and values (for loop?)
class Card:

	def __init__(self,value,suit):

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


	# function for dealing the cards to players (pop it)
	# def draw_card(cards_to_draw,player):

	# 	temp = cards_to_draw
	# 	temp_player = player
		
	# 	while temp > 0:
	# 		rand_card = random.randint(0,len(deck_used)-1)
	# 		temp_player.append(deck_used.pop(rand_card))
	# 		temp -= 1


class Deck:

	def __init__(self):
		self.cards = []
		self.make_deck()


	def make_deck(self):
		for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
			for v in range(2,15):
				self.cards.append(Card(v,s))

	def show(self):
		for c in self.cards:
			c.show()



pachet = Deck()
pachet.show()


	# def test():
	# 	print(player1)
	# 	print(player2)
	# 	print(player3)
	# 	print(player4)



# def ai_acool_first(player):
# 	# organize cards in 4 groups after colour
# 	hand=player
# 	Spades=[]
# 	Clubs=[]
# 	Hearts=[]
# 	Diamonds=[]

# 	def order_cards(suit):
# 		for s in hand:
# 			if suit in hand:
# 				suit.append(hand[s])
# 		print(suit)

# 	order_cards("Spades")


