"""
How it works:
- You want to see from what floor you can drop an egg without breaking it
- If an egg does not break, you can use it again
- You want to find this out in the most efficient way
- x = amount of eggs
- k = floors

---

My solution:
============
1 egg:
- Start from first floor, drop 1 by 1

2 eggs:
- First egg:
> Drop from floor n, then next floor is n + n - 1
> If it breaks, you know the egg will be after the previous drop, and under the
  last drop
> Big Oh = n
> n + n-1 + n-2 + ... + 2 + 1
> To find n in constant time use ceiling of the quadratic formula:
> n = ceil((-1 + sqrt(1 + 8k)) / 2)
- Second egg:
> Drop egg from floor above last tested floor where it did not break
> Keep repeating until egg breaks or until you are at floor underneath floor
  where first egg broke

2+ eggs:
- while x > 2:
> Use binary search - if egg breaks, look in half below, if it doesn't, look
  in half above
> Repeat until 2 eggs remain
- x == 2:
> See method above for 2 eggs but amount of floors = floors remaining to be
  tested
- Big Oh = ceil((-1 + sqrt(1 + (8k / 2^(x-2))) / 2) + x-2
"""
import math


baf = 0


def egg_dropper(floors = 100, eggs = 2, breaks_at_floor = 40):
    global baf
    baf = breaks_at_floor
    if eggs == 1:
        return _one_egg(floors)
    elif eggs == 2:
        return _two_eggs(floors)
    else:
        return _binary_search(eggs, floors)


def _binary_search(eggs, right, left = 1):
    if eggs == 2:
        return _two_eggs(right, left)
    if left == right:
        if left < baf:
            return left
        return left - 1
    m = left + ((right - left) // 2)
    if baf <= m:
        right = m
    else:
        left = m + 1
    return _binary_search(eggs - 1, right, left)


def _two_eggs(floors, start = 1):
    n = math.ceil((-1 + math.sqrt(1 + 8 * (floors - (start - 1)) / 2)))
    previous_floor = start - 1
    current_floor = start + n
    while current_floor <= floors:
        # 14
        if baf <= current_floor:
            return _one_egg(current_floor - 1, previous_floor + 1)
        n -= 1
        if current_floor + n > floors:
            return _one_egg(floors, current_floor)
        previous_floor = current_floor
        current_floor += n
    raise Exception("Error at two_eggs")


def _one_egg(floors, start = 1):
    current = start
    while current <= floors:
        if baf <= current:
            break
        current += 1
    return current - 1