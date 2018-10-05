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
drawed_card = []

# draw a random card (pop it)
def draw_card(cards_to_draw):

	temp = cards_to_draw
	
	while temp > 0:
		rand_card = random.randint(0,len(deck_used))
		drawed_card.append(deck_used.pop(rand_card))
		temp -= 1




def test():
	print(drawed_card)



make_deck()
draw_card(2)
test()