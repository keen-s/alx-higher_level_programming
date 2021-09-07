#!/usr/bin/python3
import random
number = random.randint(-10000,10000)
lastno = abs(number) % 10
print("Last digit of {} is {}".format(number, lastno),end=" ")
if lastno > 5:
    print("and is greater than 5")
elif lastno == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
