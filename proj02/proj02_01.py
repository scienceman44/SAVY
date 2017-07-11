# Name:
# Date:

    result = 0
    loop_control = True
while loop_control == True:
    b = int(raw_input('Enter a number to add, or 0 to indicate you are finished:'))
    if b == 0:
        loop_control = False
    result = result + b
print 'your result is:'
print result


