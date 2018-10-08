a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = []

ins = int(input("insert : "))
for x in a:
	if x < ins:
		new_a.append(x)

print(new_a)