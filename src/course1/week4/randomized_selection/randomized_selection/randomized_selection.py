from typing import List, Tuple

from numpy import random


def randomized_selection(array: List[int], select_i: int) -> int:
    if len(array) == 1:
        return array[0]

    pivot = choose_pivot(array)
    array[0], array[pivot] = array[pivot], array[0]
    array, previous_pivot = partition(array)

    if len(array) > 1:
        if previous_pivot == select_i:
            return array[previous_pivot]
        elif previous_pivot > select_i:
            return randomized_selection(array[:previous_pivot], select_i)
        elif previous_pivot < select_i:
            return randomized_selection(
                array[previous_pivot + 1 :], select_i - previous_pivot - 1
            )


def partition(array: List[int]) -> Tuple[List[int], int]:
    i = 1
    for j in range(1, len(array)):
        if array[j] < array[0]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[0], array[i - 1] = array[i - 1], array[0]
    return array, i - 1


def choose_pivot(array: List[int]) -> int:
    return random.randint(0, len(array) - 1)
