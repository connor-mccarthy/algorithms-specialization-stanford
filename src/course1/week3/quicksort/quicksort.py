from typing import List, Optional

from numpy import random

# i = boundary between non-pivot elements we've looked at and those we haven't
# j = boundary between elements less than pivot and those greater than pivot

array = [3, 2, 8, 5, 1, 4, 7, 6]
left = 0
right = len(array)

args = (array, left, right)


def choose_pivot(array: List[int], left: int, right: int) -> int:
    return random.randint(left, right)


def make_pivot_first(array: List[int], left: int, i: int) -> None:
    array[left], array[i] = array[i], array[left]


def partition(array: List[int], left: int, right: int) -> int:
    i = left + 1
    for j in range(left + 1, right):
        if array[j] < array[left]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[left], array[i - 1] = array[i - 1], array[left]

    return i - 1


def quicksort(array: List[int], left: int, right: int) -> Optional[List[int]]:
    """>=Theta(n logn), <= Theta(n**2), but typically O(n logn) in practice"""
    if len(array) in [0, 1]:
        return array

    if left < right:
        new_pivot = partition(array, left, right)

        quicksort(array, left, new_pivot)
        quicksort(array, new_pivot + 1, right)
