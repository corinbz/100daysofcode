#Reading contents of a file and printing out how many types a certain item is in the text.

with open('namelist.txt' , "r") as read_file:
	all_text = read_file.read()
	all_text = all_text.split("\n")

names = {}

for name in all_text:
	if name not in names.keys():
		names.update({name : 1})
	else:
		names[name] = names[name] + 1


print(names)