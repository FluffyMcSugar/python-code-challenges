import math


"""
Scale of truth:
- You have to calculate big Oh
- How many weightings will you maximum need to find outlier?
- In this example balls are use, all weigh even, but one is heavier

...

Scale of truth thought process:
===============================
Scenario 1 - You are given an even amount of balls:
- On each side of the scale you put same amount of balls.
- The side that's heavier will have the heavier ball.
- repeat process.
- similar to binary search

Scenario 2 - You have an uneven amount of balls:
- keep one ball to the side
- apply the rules of scenario 1
- in case the scale is in balance, the outlyer is the ball that was kept on
the side.

Thus:
1. Put same amount of balls on each side of the scale, if necessary you keep
a ball on the side
2. Repeat for the heavier side of the scale until:
    2a. Only 1 ball remains
    2b. The scale is even -> the ball kept on the side is the outlier
    2c. The scale is even, no balls are kept on the side -> error, no outlier 
"""


def scale_of_truth(amount):
    # n = 0
    # while 1 < amount:
    #     amount = amount // 2
    #     n += 1
    # return n
    # Code above equals (but is less efficient then):
    return math.floor(math.log2(amount))


if "__main__" == __name__:
    print(scale_of_truth(70))