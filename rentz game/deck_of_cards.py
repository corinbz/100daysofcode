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

deck_used = make_deck()
player1 = []
player2 = []
player3 = []
player4 = []

# draw a random card (pop it)
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





draw_card(13,player1)
# print(len(deck_used))
draw_card(13,player2)
draw_card(13,player3)
draw_card(13,player4)

test()