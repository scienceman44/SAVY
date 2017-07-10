# Name:aaron
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
y = raw_input('enter your name:')
b = raw_input('enter your age:')
x = raw_input('enter the year:')
l = raw_input('have you had a birthday yet this year?:')
result = float(x) - float(b) + 100
if l == 'yes':
    result = result+0
elif l == 'no':
    result = result-1
print (y), 'will turn 100 in the year', result
if int(b) < 13:
    print "you can watch G and PG rated movies "
elif int(b) <= 17:
    print "you can see G , PG, and PG-13 Rated movies"
elif int(b) >= 18:
    print "you can see G, PG, PG-13, and R rated movies "
