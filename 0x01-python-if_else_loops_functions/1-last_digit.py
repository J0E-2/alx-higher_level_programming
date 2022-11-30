#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def check(number):
    if number < 0:
        if (-number) % 10 == 0:
            return(f"and is 0")
        else:
            return(f"and is less than 6 and not 0")

    else:
        if number % 10 > 5:
            return(f"and is greater than 5")
        elif number % 10 == 0:
            return(f"and is 0")
        elif number % 10 < 6 and not 0:
            return(f"and is less than 6 and not 6")

if number < 0:
    print(f'Last digit of {number} is {-((-number) % 10)} {check(number)}')        
else:
    print(f'Last digit of {number} is {number % 10} {check(number)}')
    
