string = "My name is Corin and i love programming"

#Function to reverse the word order
def reverse_string():
	spl_str = reversed(string.split(" "))
	new_str = []
	
	for item in spl_str:
		new_str.append(item)
	string_rev = " ".join(new_str)
	print(string_rev)

reverse_string()