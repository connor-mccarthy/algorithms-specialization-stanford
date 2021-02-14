from typing import List, Optional

from numpy import random

# i = boundary between non-pivot elements we've looked at and those we haven't
# j = boundary between elements less than pivot and those greater than pivot


def quicksort(
    array: List[int], left: Optional[int] = None, right: Optional[int] = None
):
    """>=Theta(n logn), <= Theta(n**2), but typically O(n logn) in practice"""
    if len(array) in [0, 1]:
        return

    left = 0 if left is None else left
    right = len(array) - 1 if right is None else right

    if left < right:
        pivot = choose_pivot(array, left, right)
        array[left], array[pivot] = array[pivot], array[left]
        previous_pivot = partition(array, left, right)

        quicksort(array, left, previous_pivot - 1)
        quicksort(array, previous_pivot + 1, right)


def partition(array: List[int], left: int, right: int) -> int:
    pivot_element = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot_element:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[left], array[i - 1] = array[i - 1], array[left]

    return i - 1


def choose_pivot(array: List[int], left: int, right: int) -> int:
    return random.randint(left, right)
