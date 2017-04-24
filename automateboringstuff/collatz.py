import sys
def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print ("%d" % (number))
    return number

try:
    n = int(input('Enter number:\n').strip())
except ValueError:
    print ('Invalid integer value input. You must enter an integer')
    sys.exit(1)
while n != 1:
    n = collatz(n)
