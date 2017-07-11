print "Hi"
print "if you please"
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
result = 0
loop_control = True
while loop_control == True:
    b = int(raw_input('Enter a number to add, or 0 to indicate you are finished:'))
    if b == 0:
        loop_control = False
    result = result + b
print 'your result is:'
print result
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
