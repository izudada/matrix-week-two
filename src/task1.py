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
		self.count += 1		# Increment count which serves as an iteration
		if self.count <= self.n:	#	Check when to stop iteration
				if self.count % 2 != 0 and self.count % 3 != 0:		# Modelling the conditions for a prime number
						result = self.count
						return result
				else:
    					return " "
		else:
    			raise StopIteration("End of iteration")
				

#	Accept n as input
num = int(input("Enter stop value/number:"))
if num < 1:
    	raise ValueError("You must enter number greater than 1")


prime_numbers = PrimeIterator(num)#
# for i in prime_numbers:	#	Printing out the prime numbers using forloop
# 		try:
# 			print(next(prime_numbers))
# 		except StopIteration:
# 			print("End of iteration")
while True:
    	print(next(prime_numbers))



# *********************************************************************************************************************************************

# Generator for prime numbers
def prime_generator(n):
	"""
		generates prime numbers from `1` to a number `n`,
		where `n` is greater than 1 
	"""
	count = 2
	num_list = iter(range(2,n))

	while True:
		element = next(num_list)
		if count < n:
			if int(element) % 2 != 0 and int(element) % 3 != 0:
				print(count, element)
				return element
				count += 1
			else:
    				return ""
		raise StopIteration("End of iteration")

# result = prime_generator(num)

# print(result)
# print(result)

