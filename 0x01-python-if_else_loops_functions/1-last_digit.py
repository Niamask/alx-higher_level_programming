#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    a = ((-1 * number) % 10) * (-1)
else:
    a = number % 10
if a < 0:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
elif a == 0:
    print(f"Last digit of {number} is {a} and is 0")
elif a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
