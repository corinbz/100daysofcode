import random



player = input("Rock, paper, scissors?")

comp = random.choice(['rock', 'paper', 'scissors'])

while player.lower() == comp:
	comp = random.choice(['rock', 'paper', 'scissors'])
	print('You both chose {}. Please make another choice'.format(player))
	player = input("Rock, paper, scissors?")

if player.lower() == "rock" and comp == "paper":
	print("You lost! Paper beats rock!")
elif player.lower() == "rock" and comp == "scissors":
	print("You won! Rock beats scissors!")
elif player.lower() == "paper" and comp == "rock":
	print("You won! Paper beats rock!")
elif player.lower() == "paper" and comp == "scissors":
	print("You lost! Scissors beats paper!")
elif player.lower() == "scissors" and comp == "paper":
	print("You won! Scissors beats paper!")
else:
	print("You lost! Rock beats scissors!")