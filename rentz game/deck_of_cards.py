import random


# Create the deck of cards with suits and values (for loop?)
def make_deck():

	suits = ['Hearts' , 'Diamonds', 'Spades', 'Clubs']
	values = range(2, 15)
	deck = []

	for s in suits:
		for v in values:
			deck.append('{} of {}'.format(v,s))


	return deck

# players hands
deck_used = make_deck()
player1 = []
player2 = []
player3 = []
player4 = []

# function for dealing the cards to players (pop it)
def draw_card(cards_to_draw,player):

	temp = cards_to_draw
	temp_player = player
	
	while temp > 0:
		rand_card = random.randint(0,len(deck_used)-1)
		temp_player.append(deck_used.pop(rand_card))
		temp -= 1

def test():
	print(player1)
	print(player2)
	print(player3)
	print(player4)


#Avoind taking hands script.
"""
-divide the hand in suits and put it in ascending order
-if the card value is lower or equal to 4 put it in premium group
-rest of the group is standard.
-try to get rid of the cards with the same colour that are the fewest and the lowest
**** Make algorithm for hand to start with? score it.
-

"""

def ai_acool_first(player):
	# organize cards in 4 groups after colour
	



draw_card(13,player1)
# print(len(deck_used))
draw_card(13,player2)
draw_card(13,player3)
draw_card(13,player4)

test()