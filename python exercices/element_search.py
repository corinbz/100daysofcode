lst = [1, 2, 5, 8, 9]

nr = 10

def el_search():
	Truth = nr in lst
	if Truth:
		print("The number is inside the list.")
	else:
		print("Number is not in the list.")

el_search()