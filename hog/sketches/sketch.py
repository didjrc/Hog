""" Checks for prime numbers 

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
Initially, let p equal 2, the first prime number.
Starting from p, enumerate its multiples by counting to n in increments of p, 
and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
Find the first number greater than p in the list that is not marked. If there was no such number, stop. 

Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.

"""

p = list(range(2,71,1))
prime = []

# From: https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
def cp(n):
	'''check if integer n is a prime'''
	if n == 2:
		return True
		prime.append(n)
	# all other even numbers are not primes
	if not n & 1: 
		return False
	# range starts with 3 and only needs to go up the squareroot of n for all odd numbers
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True
	prime.append(n)