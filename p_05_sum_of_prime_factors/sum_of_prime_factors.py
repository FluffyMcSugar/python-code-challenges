from p_01_prime_number_finder import prime_number_finder as pnf


def sum_of_prime_factors(value: int) -> int:
    """ sum of prime numbers
    ...
    How it works:
    =============
    1. Find all prime numbers up to n
    2. Evaluate if n is in tuple
    3. No?
        3a. try to divide by current number in prime tuple, started at index 0
        3b. is division whole number?
        3c. Yes?
            3c1. n <- the new divided number
            3c2. add prime number to current sum
        3d. No?
            3d1. move pointer on prime tuple one to the right
            3d2. leave n as it is
        3e. Go back to step 2
    4. Yes?
        4a. add n to current sum
    5. return sum
    ...
    :param value:
    :return total_sum:
    """
    total_sum = 0
    i = 0
    prime_tuple = pnf.prime_number_finder(value)
    while value not in prime_tuple:
        evaluate_division = value / prime_tuple[i]
        if evaluate_division.is_integer():
            total_sum += prime_tuple[i]
            value = int(evaluate_division)
        else:
            i += 1
    total_sum += value
    return total_sum


if __name__ == "__main__":
    n = 42
    print(sum_of_prime_factors(8))