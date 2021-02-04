from typing import List, Tuple


def brute_force(array: List[int]) -> int:
    """O(n**2)"""
    inversion_count = 0
    for i, first_val in enumerate(array):
        for second_val in array[i:]:
            if first_val > second_val:
                inversion_count += 1
    return inversion_count


def inversion_counter(array: List[int]) -> Tuple[List[int], int]:
    """O(n*logn)"""
    if len(array) in [0, 1]:
        return array, 0

    left, right = split_array(array)
    left_sorted, left_inversions = inversion_counter(left)
    right_sorted, right_inversions = inversion_counter(right)
    sorted_array, split_inversions = merge_and_count_split_inv(
        left_sorted, right_sorted
    )
    total_inversions = left_inversions + right_inversions + split_inversions
    return sorted_array, total_inversions


def split_array(array: List[int]) -> Tuple[List[int], List[int]]:
    split_idx = len(array) // 2
    return array[:split_idx], array[split_idx:]


def merge_and_count_split_inv(a: List[int], b: List[int]) -> Tuple[List[int], int]:
    split_inversions = 0
    i = 0
    j = 0
    output = []
    for _ in range(len(a + b)):
        if i == len(a):  # handle cases where fall off a
            output.append(b[j])
            j += 1
            split_inversions += len(a[i:])
        elif j == len(b):  # handle cases where fall off b
            output.append(a[i])
            i += 1
        elif a[i] < b[j]:  # main merge procedure
            output.append(a[i])
            i += 1
        elif b[j] < a[i]:  # main merge procedure
            output.append(b[j])
            j += 1
            split_inversions += len(a[i:])
        elif a[i] == b[j]:  # handle same elements
            output.append(a[i])  # the first "if" will catch the corresponding b element
            i += 1
    return output, split_inversions
