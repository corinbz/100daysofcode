import random

a = []
b = []

for x in range(10):
	a.append(random.randint(1,5))
for x in range(15):
	b.append(random.randint(1,5))

print(a)
print(b)

def overlap():
	c = []

	for i in a:
		if i in b and i not in c:
			c.append(i)
	print(c)


overlap()