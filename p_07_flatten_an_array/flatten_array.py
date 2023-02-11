"""
Flatten an array:
---
input: array
output: a new flattened array
---
This algorithm will create a new flattened array, without modifying the
original array.
"""


def flatten_array(array) -> list:
    flattened_array = []
    _recursive_flatten_array(array, flattened_array)
    return flattened_array


def _recursive_flatten_array(old_array: list, new_array:list) -> None:
    for i in old_array:
        if isinstance(i, list):
            _recursive_flatten_array(i, new_array)
        else:
            new_array.append(i)


if __name__ == "__main__":
    array = [1,[2,7,[3,4],5],[6]]
    print(f"old array\t{array}\n"
          f"new array\t{flatten_array(array)}\n")