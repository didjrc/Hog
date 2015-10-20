dice = [4,2,3,3,4,1]
dice_total = []

def is_prime(n):
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
    for i in dice_total:
        if i == 1:
            return sum(dice_total)*0
    return sum(dice_total)
    # END Question 1

def take_turn(num_rolls, opponent_score, dice):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.

    Condition: Free Bacon. A player who chooses to roll zero dice scores one more than the largest digit in the opponent's total score.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    
    # BEGIN Question 2
    """Condition: Free Bacon"""
    if num_rolls == 0:
        #oppScore is the points earned by current player under the Condition: Free Bacon.
        oppScore = 1 + int(max(str(opponent_score)))
        return oppScore
    else:
        total = roll_dice(num_rolls, dice)

        """Condition: Hogtimus Prime"""
        if is_prime(total) is True:
            # Need to find the next prime number after prime number dice_total      
            maxPrime = list(range(total+1, total*2-1,1))
            for j in maxPrime:
                is_prime(j)
                if is_prime(j) is True:
                    return j
                    break
                else:
                    maxPrime = list(range(total+2,total*2-1,1))
                    for j in maxPrime:
                        is_prime(j)
                        if is_prime(j) is True:
                            return j
                            break
        return total
    # END Question 2