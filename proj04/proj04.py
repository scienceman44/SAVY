# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
loop_control = True
g = []
p = []
j = raw_input('I am the computer')
h = raw_input('I calculate palindromes')
k = raw_input('I know all')
while loop_control == True:
    d = raw_input('type a word for me to calculate')
    v = raw_input('calclulating ... %0')
    v = raw_input('calclulating ... %17')
    v = raw_input('calclulating ... %21')
    v = raw_input('calclulating ... %34')
    v = raw_input('calclulating ... %43')
    v = raw_input('calclulating ... %50')
    v = raw_input('calclulating ... %62')
    v = raw_input('calclulating ... %74')
    v = raw_input('calclulating ... %86')
    v = raw_input('calclulating ... %99')
    l = raw_input('Done!')
    n = raw_input('Press ENTER for your result.')
    for letter in d:
        p.append(letter)
    p.reverse()
    for letter in d:
        g.append(letter)
    if p == g:
        print d,'is a palandrome'
    elif p != g:
        print d,'is not a palandrome'
    a = raw_input('yould you like me to calclulate another word? (yes or no)')
    if a == 'yes':
        print 'ok!'
    elif a == 'no':
        print 'ok!'
        loop_control = False