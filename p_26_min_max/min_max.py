"""
MinMax
======

Find minimum and maximum value out of x amount of lists.
"""
import sys


def min_max():
    number_of_lists = int(input("How many lists would you like to evaluate? "))
    string = ""
    for i in range(number_of_lists):
        my_list = input("Input values, separate with \" \"\n> ").split()
        my_list = map(int, my_list)
        minimum, maximum = _min_max_finder(my_list)
        string += f"{i + 1}\t{minimum}\t{maximum}\n"
    return string


def _min_max_finder(list):
    minimum = sys.maxsize
    maximum = sys.maxsize * -1
    for i in list:
        if i < minimum:
            minimum = i
        if maximum < i:
            maximum = i
    return minimum, maximum


if "__main__" == __name__:
    print(min_max())
