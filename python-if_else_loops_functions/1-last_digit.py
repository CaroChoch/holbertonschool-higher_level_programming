#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdigit = number % 10
else:
    lastdigit = number % -10
if lastdigit > 5:
    print("Last digit of {:d} is {:d}".format(number, lastdigit), end=' ')
    print("and is greater than 5")
elif lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastdigit))
else:
    print("Last digit of {:d} is {:d}".format(number, lastdigit), end=' ')
    print("and is less than 6 and not 0")