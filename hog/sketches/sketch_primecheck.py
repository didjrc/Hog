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
p = list(range(2,99,1))
# range starts with 3 and only needs to go up the squareroot of n for all odd numbers
# m = list(range(3, int(max(p)**0.5)+1, 2))
# List container for Prime Numbers
prime = [] 

# From: https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python
def is_prime(n):
    """Check if integer n is a prime"""
    if n == 2:
        prime.append(n)
        return True
    if n == 3:
        prime.append(n)
        return True
    # all other even numbers are not primes
    if n%2 == 0:
        return False
    # checks remaining odd numbers
    # modified for statements to account for cases where only 1 dice is rolled with value < 3
    if int(sum(p)**0.5)+1 <= 3:
        for x in list(range(3, 5, 2)):
            if n % x == 0:
                return False
            else:
                prime.append(n) 
                return True
    else:
        for x in list(range(3, int(sum(p)**0.5)+1, 2)):
            if n % x == 0:
                return False
            else:
                prime.append(n) 
                return True

def next_prime(i):
    for i in p:
        is_prime(i)

    """ Find next prime number in sequence """
    roof = max(prime)*2
    # Need to find the next prime number after max(PRIME)       
    maxPrime = list(range(max(prime)+2,roof,1))
    for s in maxPrime:
        if is_prime(s) == True:
            print("True", s)
            break

    print("All of the primes between ", min(p), " & ", max(p), ":", prime)
    print("Found next highest prime to be: ", max(prime))