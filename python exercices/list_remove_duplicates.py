lst = [1, 2, 87, 2, 4, 7, 1, 5, 6, 8, 8]



def rem_dup():
	temp = []
	for x in range(len(lst)):
		if lst[x] in lst[x+1:]:
			pass
		else:
			temp.append(lst[x])
	print(temp)

def rem_dup2():
	temp = []
	for i in set(lst):
		temp.append(i)
	print(temp)

rem_dup()
rem_dup2()