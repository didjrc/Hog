""" Checks for prime numbers 

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
Initially, let p equal 2, the first prime number.
Starting from p, enumerate its multiples by counting to n in increments of p, 
and mark them in the list (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
Find the first number greater than p in the list that is not marked. If there was no such number, stop. 

Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.

"""

# full range of possible sum(dice) when rolling 10 dice w/ max value 7
p = list(range(2,71,1))
# range starts with 3 and only needs to go up the squareroot of n for all odd numbers
m = list(range(3, int(max(p)**0.5)+1, 2))
prime = []

# From: https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
def cp(n):
	'''check if integer n is a prime'''
	if n == 2:
		prime.append(n)
		return True
	# all other even numbers are not primes
	if n%2 == 0:
		return False
	# checks remaining odd numbers
	for x in m:
		if n % x == 0:
			return False
		else: 
			prime.append(n)
			return True

for i in p:
	cp(i)
	print(prime)