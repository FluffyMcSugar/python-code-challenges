"""
Prime number finder will show all prime numbers up to value
"""
import time

import matplotlib.pyplot as plt


def prime_number_finder(n) -> tuple:
    index = 0
    closed_list = ()
    prime_list = []
    for i in range(2, n + 1):
        if i not in closed_list:
            help_int = i
            prime_list.append(i)
            while help_int <= n:
                index += 1
                if help_int not in closed_list:
                    closed_list += help_int,
                help_int += i
    return tuple(prime_list)


# Prime number finder under test
def _calculate_time(function, arg) -> tuple:
    start_time = time.time()
    output = function(arg)
    return arg, time.time() - start_time, output


if __name__ == "__main__":
    i = 2
    x_array = []
    y_array = []
    while i <= 10000:
        x, y, output = _calculate_time(prime_number_finder, i)
        x_array.append(x)
        y_array.append(y)
        i *= 2
    plt.plot(x_array, y_array)
    plt.show()
    print(prime_number_finder(10))