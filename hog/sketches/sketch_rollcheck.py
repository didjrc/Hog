dice = [4,2,3,3,4,1]

def cp(n):
    """Check if integer n is a prime"""
    if n == 2:
        return True
    if n == 3:
        return True
    # all other even numbers are not primes
    if n%2 == 0:
        return False
    # checks remaining odd numbers
    for x in list(range(3, int(sum(dice)**0.5)+1, 2)):
        if n % x == 0:
            return False
        else: 
            return True

def roll_dice(n, dice):
    
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(n) == int, 'num_rolls must be an integer.'
    assert n > 0, 'Must roll at least once.'
    # BEGIN Question 1
    curr_roll = 0
    dice_total = []
    while curr_roll < n:
        
        """Condition: Pig Out"""
        #Checks to see whether or not an element i in dice_total is == 1.
        dice_total.append(dice[curr_roll])
        curr_roll = curr_roll + 1
        #test
        for i in dice_total:
            if i == 1:
                pigout = 1
            else:
                pigout = 0
    if pigout:
        return sum(dice_total)*0
    else:
        return sum(dice_total)
    
# """Condition: Hogtimus Prime"""
        # m = list(range(3, int(sum(dice_total)**0.5)+1, 2))
        # if cp(sum(dice_total)) == True:
        #     # Need to find the next prime number after max(PRIME)       
        #     maxPrime = list(range(sum(dice_total)+1, sum(dice_total)*2-1,1))
        #     for j in maxPrime:
        #         cp(j)
        #         if cp(j) == True:
        #             return j
        #             break
        # else:
        #     maxPrime = list(range(sum(dice_total)+2,sum(dice_total)*2-1,1)
        #     for j in maxPrime: """need to figure out why this is a Syntax error"""
        #         cp(j)
        #         if cp(j) == True:
        #             return j
        #             break
    # END Question 1