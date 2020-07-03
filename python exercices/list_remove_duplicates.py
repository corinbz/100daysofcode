lst = [1, 2, 87, 2, 4, 7, 1, 5, 6, 8, 8]



def rem_dup():
	temp = [lst[x] for x in range(len(lst)) if lst[x] not in lst[x+1:]]
	print(temp)

def rem_dup2():
	temp = [i for i in set(lst)]
	print(temp)

rem_dup()
rem_dup2()