def odd_or_even():
	num = input("Insert a number to be divided: ")
	div = input("Insert the number that divides: ")

	if int(num) % int(div) == 0:
		print("The number is evenly divisible!")
	else:
		print("The number is not evenly divisible!")

odd_or_even()