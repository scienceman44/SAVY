# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right.  Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
l = raw_input('would you like to play a guesing game?')
l = raw_input('it doesn`t matter cause you have to!!!! >:)')
l = raw_input('so here we go!!! ')
x = True
import random
answer = random.randint(1,9)
Guesses =random.randint (1,7)
while x == True:
    n = int(raw_input('I am thinking of a number 1 to 9 can you guess it?'))
    #elif answer == (10,25):
        #n = raw_input('I am thinking of a number 10 to 25, can you guess it?')
        #Guesses = Guesses + 5
    #elif answer == (16,100,):
       # n = raw_input("I am thinking of a number from 16 to 100 ca you guess it")
    if answer != n:
        Guesses = Guesses - 1
        print 'look out you only have', Guesses, 'guesses left !!'
        if Guesses == 0:
            print 'you ran out of lives :('
            print 'the number was',answer
            x = False
        if n > answer:
            print 'that guess was too high'
        if n < answer:
            print 'that guess was too low'
    elif answer == n:
        print 'GOOD JOB YOU GUESSED CORECTILY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        x = False
