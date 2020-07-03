import random

a = [random.randint(1,5) for _ in range(10)]
b = [random.randint(1,5) for _ in range(15)]

print(a)
print(b)

def overlap():
	c = []

	for i in a:
		if i in b and i not in c:
			c.append(i)
	print(c)


overlap()