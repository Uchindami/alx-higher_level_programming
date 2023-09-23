#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_figure = abs(number) % 10

if number < 0:
    last_figure = -last_figure
print("Last digit of {} is {} and is ".format(number, last_figure), end="")
if last_figure > 5:
    print("greater than 5")
elif last_figure == 0:
    print("0")
else:
    print("less than 6 and not 0")
