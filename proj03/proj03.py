# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
Guesses = 5
import random
x = True
answer = random.randint(1,9)
while x == True:
    n = raw_input('I am thinking of a number 1 to 9 can you guess it?')
    if answer != n:
        Guesses = Guesses - 1
        print 'look out you only have' ,Guesses, 'gueses left!!'
    while x == True:
        if Guesses == 0:
            print 'you ran out of lives :('
        x = False
    elif answer == n:
    print 'GOOD JOB YOU GUESED CORECTILY'
        x = False

