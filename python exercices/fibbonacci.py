def fib(nmr):
	li = [1]
	if nmr == 1:
		print(li)
	else:
		li = [1,1]
		for x in range(1, nmr-1):
			li.append(li[x-1]+ li[x])
		print(li)

fib(7)