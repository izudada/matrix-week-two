#	Collect user upper bound/n
limit =  int(input("Enter your upper limit for the prime generator: "))

class PrimeIterator:
    	
	"""
			create an iterator class named `PrimeIterator` that generates prime numbers from `1` to a number `n`,
			where `n` is greater than 1, which stops the iteration with the appropriate exception
			when it gets to a number greater than `n`
	"""

	def __init__(self, n):
		self.n = n
		self.ini = 3

	def __iter__(self):
		return self

	def __next__(self):
		result = list()
		for num in range(self.ini, self.n + 1):
			# all prime numbers are greater than 1
			if num > 1:
				for i in range(3, num):
					if (num % i) == 0:
						break
					else:
						result.append(num)
		return result

# result = PrimeIterator(limit)
# print(next(result))
# print(next(result))
# print(next(result))

# *********************************************************************************************************************************************

# Generator for prime numbers
def prime_generator(n):
	"""
		generates prime numbers from `1` to a number `n`,
		where `n` is greater than 1 
	"""
	for num in range(3, n + 1):
		# all prime numbers are greater than 1
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				yield num

# primes = prime_generator(limit)

# print(next(primes))
# print(next(primes))

