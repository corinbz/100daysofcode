import random

# Game rules:
# Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes 
# throughout teh game and tell the user at the end.


def game():
	number = random.randint(1000,10000)
	number = str(number)
	print(number)
	user_input = str(input("Please insert a 4 digit number: "))
	cow = 0
	bull = 0

	# for n in range(4):
	# 	cow = 0
	# 	bull = 0
	# 	if number[n] == user_input[n]:
	# 		cow += 1
	# 	elif user_input[n] in number:
	# 		bull += 1
	# print(cow, bull)

	while user_input != number:
			cow = 0
			bull = 0
		user_input = str(input("Please make another try: "))
		for n in range(4):
			if number[n] == user_input[n]:
				cow += 1
			elif user_input[n] in number:
				bull += 1
		print(cow, bull)




game()