import os
from typing import Callable, List, Optional


def get_data() -> List[int]:
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "quicksort_assignment_data.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [int(number.strip()) for number in lines]


def quicksort(
    array: List[int],
    choose_pivot: Callable[[List[int], int, int], int],
    left: Optional[int] = None,
    right: Optional[int] = None,
):
    """>=Theta(n logn), <= Theta(n**2), but typically O(n logn) in practice"""
    if len(array) in [0, 1]:
        return

    left = 0 if left is None else left
    right = len(array) - 1 if right is None else right

    if left < right:
        pivot = choose_pivot(array, left, right)
        array[left], array[pivot] = array[pivot], array[left]
        split_marker = partition(array, left, right)

        global comparisons
        comparisons += len(array[left:right])

        quicksort(array, choose_pivot, left, split_marker - 1)
        quicksort(array, choose_pivot, split_marker + 1, right)


def partition(array: List[int], left: int, right: int) -> int:
    pivot_element = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot_element:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[left], array[i - 1] = array[i - 1], array[left]

    return i - 1


def first_element_pivot(array: List[int], left: int, right: int) -> int:
    return left


def last_element_pivot(array: List[int], left: int, right: int) -> int:
    return right


def is_even_length(array: List[int]) -> bool:
    return len(array) % 2 == 0


def median_of_three_pivot(array: List[int], left: int, right: int) -> int:
    length = len(array[left : right + 1])
    middle = int(left + length / 2 - 1 if length % 2 == 0 else left + length // 2)
    options = [left, middle, right]
    return sorted(options, key=lambda x: array[x])[1]


choose_pivot_functions = [
    first_element_pivot,
    last_element_pivot,
    median_of_three_pivot,
]

unsorted = get_data()

comparison_list = []
for choose_pivot in choose_pivot_functions:
    comparisons = 0
    input_array = get_data()
    quicksort(input_array, choose_pivot)
    assert input_array == sorted(unsorted)
    comparison_list.append(comparisons)

results = dict(zip([func.__name__ for func in choose_pivot_functions], comparison_list))
print(results)
