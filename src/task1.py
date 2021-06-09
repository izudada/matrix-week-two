class PrimeIterator:
    	
	"""
			create an iterator class named `PrimeIterator` that generates prime numbers from `1` to a number `n`,
			where `n` is greater than 1, which stops the iteration with the appropriate exception
			when it gets to a number greater than `n`
	"""

	def __init__(self, n):
		self.n = n
		self.count = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.count += 1	
		if self.count <= self.n:
				if self.count % 2 != 0:
						result = self.count
						return result
		else:
    			raise StopIteration("End of iteration")


num = int(input("Enter stop value/number:"))
if num < 1:
    	raise ValueError("You must enter number greater than 1")

prime_numbers = PrimeIterator(num)
for i in prime_numbers:
		print(next(prime_numbers))






# Generator for prime numbers
def prime_generator(n):
    	pass

