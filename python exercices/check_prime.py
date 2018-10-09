
def is_prime(num):
	for n in range(2,num):
		if num % n == 0:
			print("The number is not prime! It divided by {}.".format(n))
			break
		else:
			continue
			print("The number is prime!")
			break

is_prime(895)