"""
Input: number, unsorted list
Output: index of number if list was sorted, returns -1 if not in list
"""


def find_in_order(n, a) -> int:
    a_copy = [i for i in a]
    a_copy.sort()
    for i in range(len(a_copy)):
        if a_copy[i] == n:
            return i
    return -1


if __name__ == "__main__":
    unsorted_list = [20,5,17,45,72,3,1, 0]
    n = 3
    expected_outcome = 2
    outcome = find_in_order(n, unsorted_list)
    print("{0:^30} | {1:^20} | {2:^20} | {3:^20}\n".format("unsorted list", "expected outcome", "actual outcome", "correct?"),
          "{0:^29} | {1:^20} | {2:^20} | {3:^20}".format(f"{unsorted_list}", f"{expected_outcome}", f"{outcome}", "CORRECT" if expected_outcome == outcome else "NOT CORRECT"))

