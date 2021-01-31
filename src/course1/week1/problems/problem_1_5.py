# Introduction Problem 5.1 You are given as input an unsorted array of n distinct numbers where n is a power of 2. Given an algorithm that identifies the second-largest number in the array, and uses t most n+log_2(n) - 2 comparisons.

from typing import List


def find_second_largest(array: List[int]) -> int:
    candidates = []

    i = 0
    for _ in array:  # n-1 pairwise comparisons
        if i >= len(array) - 1:
            break

        element_1 = array[i]
        element_2 = array[i + 1]

        if element_1 > element_2:
            candidates.append(element_2)
        elif element_2 > element_1:
            candidates.append(element_1)

        i += 2

    second_largest = candidates[0]
    for j in range(1, len(candidates)):  # log2(n)-1 comparisons
        if candidates[j] > second_largest:
            second_largest = candidates[j]

    # total = n-1 + log2(n)-1 = n + log2(n) - 2 comparisons
    return second_largest
