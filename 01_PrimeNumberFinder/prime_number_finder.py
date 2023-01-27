"""
Prime number finder will show all prime numbers up to n
"""
import time

import matplotlib.pyplot as plt


def prime_number_finder(n) -> tuple:
    index = 0
    closed_list = ()
    prime_list = []
    for i in range(1, n + 1):
        if i == 1:
            closed_list += i,
            prime_list.append(i)
        elif i not in closed_list:
            help_int = i
            prime_list.append(i)
            while help_int <= n:
                index += 1
                closed_list += help_int,
                help_int += i
    return tuple(prime_list)


# Prime number finder under test
def calculate_time(function, arg) -> tuple:
    start_time = time.time()
    function(arg)
    return arg, time.time() - start_time


if __name__ == "__main__":
    i = 2
    x_array = []
    y_array = []
    while i <= 60000:
        x, y = calculate_time(prime_number_finder, i)
        x_array.append(x)
        y_array.append(y)
        i *= 2
    plt.plot(x_array, y_array)
    plt.show()
