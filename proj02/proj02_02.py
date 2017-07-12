# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
before = 0
previous = 0
current = 1
loop_control = True
counter = 0
x = int(raw_input('How many numbers in the Fibonacci sequence would you like me to generate? :' ))
while loop_control == True:
    before = before + 1
    next = current + previous
    previous = current
    current = next
    print '#',before ,'--->' ,previous
    counter = counter + 1
    if counter == x:
        loop_control = False
