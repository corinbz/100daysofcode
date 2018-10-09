import random



def guess():

	game = True
	tries = 1
	number = random.randint(1,9)
	guess = int(input("Guess a number between 1 and 9!\n"))

	while guess not in range(1,9):
		print("The number is not in range.")
		guess = int(input("Please enter a number between 1 and 9!\n"))

	while game:

		if guess == number:
			print("You won!")
			print("The answer was {}.You got the right number in {} tries.".format(number,tries))
			game = False
		elif guess < number:
			guess = int(input("Too low!Guess higher:\n"))
			tries += 1
			continue
		else:
			guess = int(input("Too high!Guess lower:\n"))
			tries += 1
			continue

guess()
again = input("Want to play again? Y/N")
while again.lower() == "y":
	guess()
	again = input("Want to play again? Y/N")
print("Oh... bye i guess!")